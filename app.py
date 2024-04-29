# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 下午3:54
# @Auther : Tiam
# @File : app
# @Project : 1688-scraper
# @Desc :
import time

from fastapi import FastAPI, Request
import uvicorn

from shop_crawler import get_shop_product
from util import logger

app = FastAPI()


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    logger.error(f'URL: {request.url}, 发生异常: {exc}')
    return {
        "status_code": 500,
        "message": "异常, 请联系管理员",
        "data": str(exc)
    }


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):  # call_next将接收request请求做为参数
    logger.debug(f'请求地址 => {request.method}:{request.url}')
    logger.debug('请求参数 => {}'.format(request.query_params))
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)  # 添加自定义的以“X-”开头的请求头
    return response


@app.get("/")
def read_root():
    return {
        "你好": "boy",
        "请访问地址": "/docs"
    }


@app.get("/shop")
async def read_item(shop_url: str, page: int = 1):
    return await get_shop_product(shop_url, page)


if __name__ == '__main__':
    uvicorn.run(app='app:app', host="0.0.0.0", port=8000, reload=True)
