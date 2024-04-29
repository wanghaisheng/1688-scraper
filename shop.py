# _*_ coding : UTF-8 _*_
# @Time : 2024/4/28 下午10:49
# @Auther : Tiam
# @File : shop
# @Project : 1688-scraper
# @Desc :
import asyncio
import json
import re

import signer
from config import *
from util import asyhttp, logger
from util import to_item, save_in_excel


async def get_shop_id(shop_url: str):
    """

    :param shop_url: like this 'https://shop49w5890640814.1688.com/page/offerlist.htm'
    :return:
    """
    params = {
        'spm': 'a2615.2177701.wp_pc_common_topnav.0',
    }

    response = await asyhttp.get(shop_url, params=params, cookies=cookies, headers=headers)
    # 正则表达式，用于匹配memberId后面的值
    pattern = r'"memberId":"([^"]+)"'
    # 使用正则表达式搜索
    match = re.search(pattern, await response.text())
    # 如果找到匹配项，则提取并打印结果
    if match:
        member_id = match.group(1)
        return member_id
    else:
        logger.error("没有找到店铺ID!")


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
    token = cookies['_m_h5_tk'].split('_')[0]

    params['t'], params['sign'] = signer.sign(data['data'], token)
    # print(params['t'], params['sign'])

    response = await asyhttp.post(
        'https://h5api.m.1688.com/h5/mtop.1688.shop.data.get/1.0/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    # print(response.text)
    return await response.json()


async def get_shop_all_product(shop_id):
    page_num = 1
    total_page = 1
    total = []
    while page_num <= total_page:
        logger.info("page: {}", page_num)
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
    url = input("请输入店铺地址: ")
    sid = await get_shop_id(url)
    # sid = "b2b-2212676093205a9a2e"
    if sid:
        logger.info("shop_id: {}", sid)
        total_product = await get_shop_all_product(sid)
        save_in_excel(total_product, sid)


if __name__ == '__main__':
    asyncio.run(main())
