# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午12:54
# @Auther : Tiam
# @File : config
# @Project : 1688-scraper
# @Desc :

import json

import redis

# 建立 Redis 连接
redis_client = redis.StrictRedis(host='47.116.210.255', port=6379, db=0, password='bwxRoot123456')


def set_cookies(cookies: dict):
    redis_client.set('cookies', json.dumps(cookies))


def get_cookies():
    cookies: bytes = redis_client.get('cookies')
    if cookies:
        return json.loads(cookies)
    # else:
    #     logger.info('请先更新cookie! Redis 中没有 cookies 缓存')


def init_cookie():
    cok = {
        "_med": "dw:2560&dh:1440&pw:2560&ph:1440&ist:0",
        "cna": "AiqqHvPsXSICAY4EfAzZI5By",
        "_bl_uid": "valbpvU1k0baIn9v1v42c5Fr6bqj",
        "hng": "CN|zh-CN|CNY|156",
        "lid": "梦仲点电店",
        "_csrf_token": "1714441545479",
        "_m_h5_tk": "49d616f7d84423ab67f084fc2fd55a3b_1714449466512",
        "_m_h5_tk_enc": "69ac3ab5c548e060b8ba5f9c79499792",
        "__cn_logon__": "false",
        "t": "31c0f03542272c9a60460e43f2f80958",
        "_tb_token_": "7bbe3e5be37b5",
        "tfstk": "f2no3KT6F4z5qMXpZmqW0SzaKqYvV_ZQIXIL9kFeuSPf2XE8vrz4IJ7PUkSd3Zy-agzUzJWV3ScQwzEzvkfn6SN-Jp978pc-dMUEvWnhFmcGvgdWPvS3vkR96hKtFYEQYCBwnZ6aNJM4T39ZoAD7AkRAHM89jYGgLz_WZkJ00JyGzkyz8oJ0p8WzY7zFgxyUgWrUYXrq3JyaTTzFYt7q6E_z6DuZ0deM2bdZaXo0ErzxUS7aNm2ur5kPJMSF584u_YPD63JxZrkQ-D6CxrHr5XwZa_RuYx2isRckJ9NouAn-8YxD_YZ3Zb0UoL-rnuVuSmUGKaro8bi3P4XBCxrrGVN_zEObn0nT-5acgQkxn7zi-bdfY73i3j4tDsIT0Au0mgkcuNPEfMw2pm7CRzybn5O5-VX0Bn61tKvcWvazhRN9nKbCRzybn5pDnNHQz-w_6",
        "isg": "BD4-ShGU1NmJ5gDh1eJs7h12j1SAfwL5gjk0x-hHsAF8i95lUAqpCFRpB9dHqPoR"
    }
    cookies = get_cookies()
    if cookies is None or '_m_h5_tk' not in cookies:
        set_cookies(cok)


init_cookie()
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
