# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午9:21
# @Auther : Tiam
# @File : util
# @Project : 1688-scraper
# @Desc :
import pandas as pd


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
        print(f'{filename}.xlsx 保存成功')
        return True
    except Exception as e:
        print(f'{filename}.xlsx 保存失败，原因：{e}')
        return False
