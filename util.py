# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午9:21
# @Auther : Tiam
# @File : util
# @Project : 1688-scraper
# @Desc : 公共方法
import asyncio

import pandas as pd
import openpyxl
import sys

from aiohttp import ClientSession, ClientTimeout
from loguru import logger as loguru_logger
from aiohttp_retry import RetryClient, ExponentialRetry
from config import log_save_path
import aiohttp


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


class AsyHttp:
    def __init__(self):

        self.retry_client = None

    async def request(self, method, url, **kwargs):
        logger.debug(f"正在发起请求 => {method}:{url}")
        try:
            # 代理: https://docs.aiohttp.org/en/stable/client_advanced.html#proxy-support
            proxy = 'http://your_proxy_url:your_proxy_port'
            proxy_auth = aiohttp.BasicAuth('your_user', 'your_password')
            # 超时
            async with ClientSession(timeout=ClientTimeout(total=10, connect=3)) as client:
                # 重试3次
                self.retry_client = RetryClient(client, retry_options=ExponentialRetry(attempts=3))
                async with self.retry_client.request(method, url, **kwargs) as response:
                    logger.debug(f"返回状态码 => {response.status}")
                    return response
        except aiohttp.ClientError as e:
            logger.error(f"请求失败 => {e}")
        finally:
            pass
            # await self.retry_client.close()

    async def get(self, url, **kwargs):
        return await self.request('GET', url, **kwargs)

    async def post(self, url, **kwargs):
        return await self.request('POST', url, **kwargs)


asyhttp = AsyHttp()

if __name__ == '__main__':
    async def main():
        resp = await asyhttp.get('https://www.baidu.com')
        print(resp.text)


    asyncio.run(main())
