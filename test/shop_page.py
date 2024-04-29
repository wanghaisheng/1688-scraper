import asyncio

import shop_crawler
from util import logger


async def main():
    shop_url = 'https://shop2260590x869h3.1688.com/page/offerlist.htm'
    shop_id = await shop_crawler.get_shop_id(shop_url)
    logger.info(f'shop_id: {shop_id}')
    return await shop_crawler.get_shop_product(shop_id)


if __name__ == '__main__':
    asyncio.run(main())
