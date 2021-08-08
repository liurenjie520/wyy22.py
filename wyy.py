# coding=utf-8
"""
从土味情话中获取每日一句。
 """
import requests
import json
from datetime import datetime


__all__ = ['get_lovelive_info']


def get_lovelive_info():

    print('获取...')
    try:
        resp = requests.get('https://tenapi.cn/comment/')
        if resp.status_code == 200:
            content_dict = resp.json()

            str25=""
            data1 = content_dict.get("data").get("content")
            data2 = content_dict.get("data").get("song") #gequ
            data3 = content_dict.get("data").get("sing")

            # result1 = []
            # for i in data:
            pkp2=data1+"\nfrom music ："+"《"+data2+"》\n"+"from artist ：@"+data3
            str25=pkp2

            return str25
        print('获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


get_one_words = get_lovelive_info

if __name__ == '__main__':

    is_tomorrow = get_lovelive_info()
    url = 'https://service-etcne5bg-1254304775.gz.apigw.tencentcs.com/release/Wecom_push'
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    dt = datetime.now()
    time = dt.strftime('%Y-%m-%d')
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData = {
        'sendkey': 'akb48',
        'msg_type': 'text',
        'msg': f'网易云热评-{time}'+'\n'+is_tomorrow

    }

    res = requests.post(url=url, json=FormData)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)

    print(is_tomorrow)
