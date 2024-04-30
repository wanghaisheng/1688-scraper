# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午9:21
# @Auther : Tiam
# @File : util
# @Project : 1688-scraper
# @Desc : 公共方法
import sys

import aiohttp
import pandas as pd
from aiohttp import ClientSession, ClientTimeout, ClientHttpProxyError, ServerDisconnectedError
from aiohttp_retry import RetryClient, ExponentialRetry
from loguru import logger as loguru_logger

import signer
from config import log_save_path, log_level, cookies


class MyLogger:
    def __init__(self, log_file_path=log_save_path):
        self.logger = loguru_logger
        # 清空所有设置
        self.logger.remove()
        # 添加控制台输出的格式,sys.stdout为输出到屏幕;关于这些配置还需要自定义请移步官网查看相关参数说明
        self.logger.add(sys.stdout,
                        format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 颜色>时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                               ":<cyan>{line}</cyan> | "  # 行号
                               "<level>{level}</level>: "  # 等级
                               "<level>{message}</level>",  # 日志内容
                        level=log_level
                        )
        # 输出到文件的格式,注释下面的add',则关闭日志写入
        self.logger.add(log_file_path + 'scraper.log', level='DEBUG',
                        format='{time:YYYYMMDD HH:mm:ss} - '  # 时间
                               "{process.name} | "  # 进程名
                               "{thread.name} | "  # 进程名
                               '{module}.{function}:{line} - {level} -{message}',  # 模块名.方法名:行号
                        rotation="10 MB")

    def get_logger(self):
        return self.logger


logger = MyLogger().get_logger()


def to_item(x):
    return {
        'subject': x['subject'],
        'underLinePrice': x['underLinePrice']
    }


def save_in_excel(data, filename):
    # 写入 excel
    try:
        df = pd.DataFrame(data)
        df.to_excel(f'output/{filename}.xlsx', index=False, engine='openpyxl')
        logger.info(f'{filename}.xlsx 保存成功')
        return True
    except Exception as e:
        logger.info(f'{filename}.xlsx 保存失败，原因：{e}')
        return False


global_proxy = None


async def update_proxy():
    global global_proxy
    url = 'https://service.ipzan.com/core-extract'
    params = {
        'num': '1',
        'no': '20240430549415161446',
        'minute': '1',
        'format': 'json',
        'protocol': '1',
        'pool': 'quality',
        'mode': 'whitelist',
        'secret': '4dmg4911mi7sgf'
    }
    try:
        async with ClientSession() as session:
            async with session.get(url, params=params) as response:
                json_data = await response.json()
                if json_data['status'] == 200 and json_data['code'] == 0:
                    proxy = json_data['data']['list'][0]
                    global_proxy = f'http://{proxy["ip"]}:{proxy["port"]}'
                else:
                    logger.error("返回错误: {}", json_data)
    except Exception as e:
        logger.error('获取代理IP失败: {}', str(e))


async def proxy_request(method, url, callback, **kwargs):
    logger.debug(f"正在发起请求 => {method}:{url}")
    retry_proxy = 3
    # 签名
    if params := kwargs.get('params'):
        token = cookies['_m_h5_tk'].split('_')[0]
        params['t'], params['sign'] = signer.sign(kwargs.get('data').get('data'), token)
    if global_proxy is None:
        await update_proxy()
    connector = aiohttp.TCPConnector(force_close=True, verify_ssl=False)
    async with ClientSession(connector=connector, timeout=ClientTimeout(total=30, connect=10), trust_env=True) as client:
        async with RetryClient(client, retry_options=ExponentialRetry(attempts=3)) as retry_client:
            try:
                logger.debug(f"代理IP => {global_proxy}")
                async with retry_client.request(method, url, proxy=global_proxy, cookies=cookies, **kwargs) as response:
                    return await callback(response)
            except (ClientHttpProxyError, ServerDisconnectedError) as e:
                retry_proxy -= 1
                if retry_proxy > 0:
                    logger.error("代理失效: {}, ", e)
                    await update_proxy()
                    logger.error("正在更换代理 => {}, 正在重试第 {} 次请求", global_proxy, 3 - retry_proxy, )
                    return await proxy_request(method, url, callback, **kwargs)
                logger.error("{} 代理错误: {}", retry_proxy, e)
            except Exception as e:
                logger.error("请求异常: {}", e)


async def proxy_get(url, callback, **kwargs):
    return await proxy_request('GET', url, callback, **kwargs)


async def proxy_post(url, callback, **kwargs):
    return await proxy_request('POST', url, callback, **kwargs)


if __name__ == '__main__':
    pass
