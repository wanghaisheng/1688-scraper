# _*_ coding : UTF-8 _*_
# @Time : 2024/4/28 下午11:20
# @Auther : Tiam
# @File : signer
# @Project : 1688-scraper
# @Desc :
import os
import time

import execjs

from config import app_key


def sign(data, m_h5_tk):
    # print("signing...", data, m_h5_tk)
    timestamp = str(int(time.time() * 1000))  # 时间戳

    p = (m_h5_tk + "&" + timestamp + "&" + app_key + "&" + data)
    path = os.path.dirname(__file__) + '\\sign.js'
    with open(path, 'r', encoding='utf-8') as f:  # 加载js
        ctx = execjs.compile(f.read())
    return timestamp, ctx.call('u', p)
