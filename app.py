# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 下午3:54
# @Auther : Tiam
# @File : app
# @Project : 1688-scraper
# @Desc :
import time

import uvicorn
from fastapi import FastAPI, Request, applications
from fastapi.openapi.docs import get_swagger_ui_html

import shop_crawler
from config import set_cookies
from util import logger

app = FastAPI()


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js',
        swagger_css_url='https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css'
    )


applications.get_swagger_ui_html = swagger_monkey_patch


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    logger.error(f'URL: {request.url}, 发生异常: {exc}')
    return {
        "status_code": 500,
        "message": "异常, 请联系管理员Moment_Shiny",
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
def hello():
    return {
        "你好": "boy",
        "请访问地址": "/docs"
    }


@app.get("/shop")
async def shop(shop_url: str = 'https://shop2260590x869h3.1688.com/page/offerlist.htm', page: int = 1):
    shop_id = await shop_crawler.get_shop_id(shop_url)
    logger.info(f'获取到店铺ID: {shop_id}')
    return await shop_crawler.get_shop_product(shop_id, page)


@app.post("/update/cookies")
async def update_cookies(cookies: dict):
    try:
        set_cookies(cookies)
        return {
            "message": "更新成功"
        }
    except Exception as e:
        return {
            "message": "更新失败 => " + str(e),
        }


if __name__ == '__main__':
    uvicorn.run(app='app:app', host="0.0.0.0", port=5000, reload=True)
