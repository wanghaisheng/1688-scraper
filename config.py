# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午12:54
# @Auther : Tiam
# @File : config
# @Project : 1688-scraper
# @Desc :
from http.cookies import SimpleCookie

cookies = {
    'cna': 'AiqqHvPsXSICAY4EfAzZI5By',
    'hng': 'CN%7Czh-CN%7CCNY%7C156',
    'lid': '%E6%A2%A6%E4%BB%B2%E7%82%B9%E7%94%B5%E5%BA%97',
    '_csrf_token': '1714477509306',
    '_m_h5_tk': '5e9de5d866f6e82d30c0d5ede1179bce_1714331984926',  # 过期版
    '_m_h5_tk_enc': '318d4161786c4ea0dff76fa08ab48e41',
    # '_m_h5_tk': 'c4d26d21258ed8ed8b3f33a49f545222_1714487950299',
    # '_m_h5_tk_enc': 'b124da850be394f329024741778129ac',
    'sgcookie': 'E100yNnOeyCir3MZSQCzAZpqGRf3ujsus%2BI6KjH%2BahxBtP2Qdmj4pg0B3XWtoudxBm4ifGH5qslDC5EEn65p2stcG9JZ%2BLU6S3FXVgeWJc3dNzGjK%2FWiNAvdX1WF5iwef0Ft',
    'uc4': 'id4=0%40UgQycz3QT6tDE5AoEbMnqmK3RVVS&nk4=0%40oib%2BOBj0WsRXrGUpZjihcqcQsoIm',
    '__cn_logon__': 'false',
    'cookie2': '109ed8fb8f25333178a190fbcef081ef',
    't': '5dbad1e854f7911e6ce1b2451390f669',
    '_tb_token_': '38e385fd69357',
    'tfstk': 'f47KnMsVeR2ht0qlR6ZGUGnWuyNgjwCE595jrLvnVOBON99HE3tSf1OD9LMoPQaswQ9MO0gSPGpRCOpBEk7nyOB1ngjHqT4JFsJGE4fhyGuRg_73TUVe868yP-20oUCFTUrXbXQ_I1NWaMSV6rUcT6ls9YNcfrmR1DmTwL6WAFM6tdOBNU6Wfh9waQMBN2NO1dRWPQ9WNfG6tI9SOpG907vs4LgRSTkHjhzXI4g55U-pH6ioP4_99HnFOdIGjNdpvKtMzQWPROf5-w-a40YPsiBRVOatJTCCcT9h5-gJEiRRNILjiVfOGQKXPhhSP1LBQh_plrM9_G1hVwWKw4OF-ZxJ3hFSz3Y1onsfpbPV1eO5Un7u32JCNs7VmEU-5eK54_bck1konKdoA5Ft40-BspS6_KUJz0cB6KVLq0oyjoO9n5Ft40-B_Cp09umr4hqf.',
    'isg': 'BBwcqgchlh8r9GLfa1hu6Cu87TrOlcC_VENWmfYdKIfqQbzLHqWQT5L3oSm5UvgX',
}


def update_cookies(request_cookie: SimpleCookie[str]):
    """
    更新 令牌
    :param request_cookie:
    :return:
    """
    global cookies
    # 更新 _m_h5_tk, _m_h5_tk_enc 键值
    cookies['_m_h5_tk'] = request_cookie['_m_h5_tk'].value
    cookies['_m_h5_tk_enc'] = request_cookie['_m_h5_tk_enc'].value


count = 30
app_key = '12574478'

# 日志配置
log_save_path = "./logs/"
log_level = "DEBUG"
