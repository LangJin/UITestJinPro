# -*- coding:utf-8 -*-
'''
时间：2017-12-29
作者：浪晋
说明：公共方法都在这里
'''
import requests
import json


def requestpost():
    url = ""
    headers = {}
    data = {}
    r = requests.post(url=url, headers=headers, data=data)
    r = json.loads(r.text)
    print(r)
