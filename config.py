# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午12:54
# @Auther : Tiam
# @File : config
# @Project : 1688-scraper
# @Desc :

import json

import redis

# 建立 Redis 连接
redis_cache = redis.StrictRedis(host='123.60.19.63', port=6379, db=0)


def set_cookies(cookies: dict):
    redis_cache.set('cookies', json.dumps(cookies))


def get_cookies():
    cookies: bytes = redis_cache.get('cookies')
    if cookies:
        return json.loads(cookies)
    # else:
    #     logger.info('请先更新cookie! Redis 中没有 cookies 缓存')


# 会过期
# cookies = get_cookies()

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shop3l10r1o282353.1688.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://shop3l10r1o282353.1688.com/',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
}

count = 30
app_key = '12574478'

# 日志配置
log_save_path = "./logs/"
log_level = "DEBUG"
