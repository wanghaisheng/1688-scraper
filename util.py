# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午9:21
# @Auther : Tiam
# @File : util
# @Project : 1688-scraper
# @Desc : 公共方法
import asyncio
import warnings

import pandas as pd
import openpyxl  # pip install openpyxl
import sys

from aiohttp import ClientSession, ClientTimeout
from loguru import logger as loguru_logger
from aiohttp_retry import RetryClient, ExponentialRetry
from config import log_save_path, log_level
import aiohttp

warnings.simplefilter('ignore', category=ResourceWarning)
# warnings.filterwarnings('ignore')

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


class AsyHttp:
    def __init__(self):
        # 默认情况下，aiohttp使用HTTP keep-alive，因此同一个TCP连接可以用于多个请求。 这可以提高性能，因为不必为每个请求都建立一个新的TCP连接。
        connector = aiohttp.TCPConnector(force_close=True)
        self.client = ClientSession(connector=connector, timeout=ClientTimeout(total=10, connect=3))
        # 重试3次
        self.retry_client = RetryClient(self.client, retry_options=ExponentialRetry(attempts=3))

    def request(self, method, url, **kwargs):
        logger.debug(f"正在发起请求 => {method}:{url}")
        try:
            # await self.semaphore.acquire()
            # async with self.semaphore:
            # 代理: https://docs.aiohttp.org/en/stable/client_advanced.html#proxy-support
            proxy = 'http://your_proxy_url:your_proxy_port'
            proxy_auth = aiohttp.BasicAuth('your_user', 'your_password')
            return self.retry_client.request(method, url, **kwargs)
        except aiohttp.ClientError as e:
            logger.error(f"请求失败 => {e}")
        finally:
            # await self.semaphore.acquire()
            # await self.retry_client.close()
            pass

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)

    async def close(self):
        await self.retry_client.close()
        await self.client.close()

    async def __aenter__(self):
        # 这里执行资源的初始化操作
        self.__init__()
        # logger.debug(f"正在初始化资源 => {self.client}")
        return self  # 返回self或其他资源供with语句中的as使用

    async def __aexit__(self, exc_type, exc_value, traceback):
        # logger.debug(f"正在关闭资源 => {self.client}")
        # 这里执行资源的清理操作
        await self.close()
        # 如果没有异常，返回False；如果处理了异常，返回True
        return False


# asyhttp = AsyHttp()

if __name__ == '__main__':
    async def main():
        async with AsyHttp() as http:
            async with http.get("http://baidu.com") as response:
                print(await response.text())


    asyncio.run(main())
