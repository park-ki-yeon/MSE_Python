#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭이라는 문자열을 최고가-최저가로 지정한다.
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
# if조건이 참이면 "상승장"을 출력한다.
if (시가+변동폭) > 최고가:
    print("상승장")
# if조건이 거짓이어서 if문이 실행되지 않을 경우 else문을 실행한다.
# "하락장"을 출력한다.
else:
    print("하락장")

