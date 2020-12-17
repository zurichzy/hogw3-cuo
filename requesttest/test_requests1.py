#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

corpid = 'ww01ad7285c3b2f87c'
corpsecret = 'hzizt4fesrs-Eg2uz8aYC4a9yZHphA32Lqb3R57Nzuw'

def get_token():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    result = requests.get(url).json()
    return result['access_token']

def test_get():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id=Zurich'
    print(requests.get(url).json())


def test_AddDp():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}'
    data = {
        "name": "测试2",
        "name_en": "test2",
        "parentid": 3,
        "order": 3,
    }
    print(requests.post(url, json=data).json())

def test_UpdateDp():
    url =f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}'
    data= {
        "id": 3,
        "name": "测试测试"
    }
    print(requests.post(url, json=data).json())

def test_Delete():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id=2'
    print(requests.get(url).json())