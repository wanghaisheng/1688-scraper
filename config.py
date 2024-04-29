# _*_ coding : UTF-8 _*_
# @Time : 2024/4/29 上午12:54
# @Auther : Tiam
# @File : config
# @Project : 1688-scraper
# @Desc :

# 会过期
cookies = {
    'EGG_SESS': 'xXWBzGzKLNeroZE7tz4XR_7B3K_Ahnd-nMzWJ39uryxys8G6puRRNFSMFdEulg1yO7VtjhwmDP4nCGo-2gNkeIAOlq9cmW30N-ckj3YtnIVr0w48vNF31fNrYg2o27WhMo1c4GemD5VmyFsE3ZY9uhL36peTBGKYkufFhpSvmqGY5oaRzP9QMwZrkouzloka',
    '_csrf_token': '1714354267804',
    'cna': 'AiqqHvPsXSICAY4EfAzZI5By',
    'cookie2': '1d8101834f9489f18f4256c0029613e0',
    'sgcookie': 'E100yNnOeyCir3MZSQCzAZpqGRf3ujsus%2BI6KjH%2BahxBtP2Qdmj4pg0B3XWtoudxBm4ifGH5qslDC5EEn65p2stcG9JZ%2BLU6S3FXVgeWJc3dNzGjK%2FWiNAvdX1WF5iwef0Ft',
    'hng': 'CN%7Czh-CN%7CCNY%7C156',
    't': '8eef8e6b50d1ff3701e6289c36e2d053',
    '_tb_token_': '58beee4e34877',
    'lid': '%E6%A2%A6%E4%BB%B2%E7%82%B9%E7%94%B5%E5%BA%97',
    'uc4': 'id4=0%40UgQycz3QT6tDE5AoEbMnqmK3RVVS&nk4=0%40oib%2BOBj0WsRXrGUpZjihcqcQsoIm',
    '__cn_logon__': 'false',
    '_m_h5_tk': 'd0547c656a7598a33cf2c0a62ccdcd31_1714384818074',
    '_m_h5_tk_enc': 'c3e42c89d7ec08d5ac7de291d1305aff',
    'tfstk': 'fvAt3h9yDDmGhTMD1FMH0yFZf_0n-CLaOh87iijghHKplhsGmt6bde_lWiZ0GZGQkZsh5-NbGpIvAHI1mARgMHKBqKvGnncAcUSHmSYMMpPvzERi7s0N_F5VG0moZsLw7s7j3rmixegfudJyJbhk7FzQWogkdb2vvBCW1itfCMNCuMw1lstfOX_fA5_b1ssIJZSCcs615WwCyar_h56s66uOYP_TMBx8kqFsmsPbGC1VBgL7nSNX9NBTQFspELAdWOI5Ks720CtHlCANLxycgevJDKtI95Kv5LtfjBi7MivPkE_RNzVHJU_AFs6LlSTd1MWB6_G7vwJBSKOwXrFf7CAlHgWKlSWcOQXWFhUqze11lnWyi0PNfETyaLf-MW1Ohg-wZQHwQujRoRgKJ-yVCwjwdwS-Msy05wIo5Ow43tbFJg0KJ-yVCw7dqV6_3-Wc8',
    'isg': 'BK6u-0ICRLb657BRxbL8vi2m_wRwr3Kpkgmkl9h3XrFsu08VQDfauFT1c6dXeGrB',
}


headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cna=AiqqHvPsXSICAY4EfAzZI5By; hng=CN%7Czh-CN%7CCNY%7C156; lid=%E6%A2%A6%E4%BB%B2%E7%82%B9%E7%94%B5%E5%BA%97; ali_apache_track=c_mid=b2b-3374346636f0ed7|c_lid=%E6%A2%A6%E4%BB%B2%E7%82%B9%E7%94%B5%E5%BA%97|c_ms=1; __mwb_logon_id__=%25E6%25A2%25A6%25E4%25BB%25B2%25E7%2582%25B9%25E7%2594%25B5%25E5%25BA%2597; taklid=d57e7f1df0914e6685df1187bb9e15a0; mwb=tm; mtop_partitioned_detect=1; _m_h5_tk=f04154127b98ebb771e678d802c5c970_1714319379159; _m_h5_tk_enc=806b8657ca6efe99baad1cc15df141f3; cookie2=177905f5f9ff50897cfe499a1b53f8ca; sgcookie=E100yNnOeyCir3MZSQCzAZpqGRf3ujsus%2BI6KjH%2BahxBtP2Qdmj4pg0B3XWtoudxBm4ifGH5qslDC5EEn65p2stcG9JZ%2BLU6S3FXVgeWJc3dNzGjK%2FWiNAvdX1WF5iwef0Ft; t=7bb642d6af15b8142cb40045f87f022d; _tb_token_=ee339eb714e77; uc4=id4=0%40UgQycz3QT6tDE5AoEbMnqmK3RVVS&nk4=0%40oib%2BOBj0WsRXrGUpZjihcqcQsoIm; __cn_logon__=false; _csrf_token=1714308951178; tfstk=fzVnnn6fRJkIC_YRx5cC_mVH45BtOHGSoud-2bnPQco69uhKwc7oy4u-8XHy7AuroBkrL48w7cqSvvhEwbxuDciLea_IUaqLPQHzw0FkR5qDwBICdzRowbSADsCYRyhSai3zzVBEA4aZ4OvFbJzINbS9WQWAiyZmXLtfEb7i_43X8bkEUP7ir4hyTYReQhoszboz4vJwQ4gDY2Rr8AlTVLi0AoFNkVobaBn-c50nLAUEbQu_s2Dn0yJJaQJI-vm48cjATv6-QzMuNUOoByybVqreYMczSqqmokXJPD2akWez-1j4Rbm3x8kG86zitDD06xYkLX2zA7DQKU_b7Xr_hmMFCGgg9SHocAxNYPUiYx2uvGOrv-4ajxF9XIhauRcG49Jw3so9NV78_L9SLVgicM9unFY8-7j1SNvf_vusR1bGSL9SLVgiDNbMh1kE521G.; isg=BDMz52wXUfQn9B0iGFXJnciZwjddaMcql4aJROXQj9KJ5FOGbThXepF6npQK3x8i',
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
log_level = "INFO"
