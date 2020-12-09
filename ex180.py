#!/usr/bin/env python
# coding: utf-8

# In[7]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
# append함수는 리스트에 요소를 추가하는 함수다.
# append함수를 사용하여 volatility리스트에 변동폭을 추가한다. 
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
# print함수를 사용하여 volatility리스트의 값을 출력한다.
print(volatility)

