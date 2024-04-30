# _*_ coding : UTF-8 _*_
# @Time : 2024/4/28 下午10:49
# @Auther : Tiam
# @File : shop
# @Project : 1688-scraper
# @Desc :
import asyncio
import json
import re
import time

import signer
from config import *
from util import logger, proxy_get, proxy_post
from util import to_item


async def get_shop_id(shop_url: str):
    """

    :param shop_url: like this 'https://shop49w5890640814.1688.com/page/offerlist.htm'
    :return:
    """
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    }

    async def callback(response):
        # 正则表达式，用于匹配memberId后面的值
        pattern = r'"memberId":"([^"]+)"'
        # 使用正则表达式搜索
        match = re.search(pattern, await response.text())
        # 如果找到匹配项，则提取并打印结果
        if match:
            member_id = match.group(1)
            return member_id
        else:
            logger.error("没有找到店铺ID! 请检查你输入的地址或稍后再试")

    return await proxy_get(shop_url, callback, headers=headers)


retry_cookie = 0


async def get_shop_product(shop_id: str, page_num: int = 1):
    params = {
        'jsv': '2.7.0',
        'appKey': app_key,
        # 't': '1714312920003',
        # 'sign': '7dd95103f3041c5ec5c122a360d7f813',
        'api': 'mtop.1688.shop.data.get',
        'v': '1.0',
        'type': 'json',
        'valueType': 'string',
        'dataType': 'json',
        'timeout': '10000',
    }
    arg_string = {
        "memberId": shop_id,
        "appName": "pcmodules",
        "resourceName": "wpOfferColumn",
        "type": "view",
        "version": "1.0.0",
        "appdata": {
            "sortType": "wangpu_score",
            "sellerRecommendFilter": False,
            "mixFilter": False,
            "tradenumFilter": False,
            "quantityBegin": None,
            "pageNum": page_num,
            "count": count
        }
    }
    body = {
        "dataType": "moduleData",
        # 再json.dumps()转回JSON会自动添加上空格
        "argString": json.dumps(arg_string, separators=(',', ':'))
    }
    data = {
        'data': json.dumps(body, separators=(',', ':')),
    }
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

    async def callback(response):
        global retry_cookie
        json_data = await response.json()
        if json_data['ret'][0] == 'SUCCESS::调用成功':
            return json_data
        retry_cookie += 1
        if retry_cookie >= 3:
            return {
                "message": "更新cookie失败, 重试次数过多",
                "json_data": json_data,
            }
        logger.error(json_data['ret'][0])
        logger.error("正在更新cookie 3秒后自动进行第 {} 次重试!", retry_cookie)
        time.sleep(3)
        update_cookies(response.cookies)
        return await proxy_post('https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/', callback, params=params, data=data, headers=headers)

    return await proxy_post('https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/', callback, params=params, data=data, headers=headers)


async def get_shop_all_product(shop_id):
    page_num = 1
    total_page = 1
    total = []
    while page_num <= total_page:
        logger.info("current page: {}", page_num)
        json_data = None
        try:
            json_data = await get_shop_product(shop_id, page_num)
            content = json_data['data']['content']

            if page_num == 1:
                offer_count = content['offerCount']
                logger.info("总商品数量: {}", offer_count)
                total_page = int(int(offer_count) / count) + 1
                logger.info("总页数: {}", total_page)

            offer_list = list(map(to_item, content['offerList']))
            total.extend(offer_list)
        except KeyError as e:
            logger.error("请尝试更新cookie! json_data: {}, E: {}", json_data, e)
        except Exception as e:
            logger.error("异常类型{}, {}", type(e), e)
            logger.error("页码: {}, E: {}", page_num, e.args)
        finally:
            page_num += 1

    return total


async def main():
    # https://shop2260590x869h3.1688.com/page/offerlist.htm
    # https://shop49w5890640814.1688.com/page/offerlist.htm
    # url = input("请输入店铺地址: ")
    url = 'https://shop2260590x869h3.1688.com/page/offerlist.htm'
    sid = await get_shop_id(url)
    logger.info("shop_id: {}", sid)
    # sid = "b2b-2212676093205a9a2e"
    # sid = "b2b-2217035390425d35e9"
    # if sid:
    #     logger.info("shop_id: {}", sid)
    #     total_product = await get_shop_all_product(sid)
    #     logger.info("total_product: {}", len(total_product))
    #     # save_in_excel(total_product, sid)


async def main2():
    res = await get_shop_product('b2b-2217035390425d35e9')
    logger.info(res)


if __name__ == '__main__':
    asyncio.run(main2())
