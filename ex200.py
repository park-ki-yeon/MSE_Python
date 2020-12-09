#!/usr/bin/env python
# coding: utf-8

# In[4]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

total_profit = 0
# for문을 사용하여 변수에 리스트의 원소들을 대입하고 수행할 문장을 반복하여 실행한다.
# profit이라는 문자열을 종가-시가로 지정한다.
for day_price in ohlc[1:]:
    profit = day_price[0] - day_price[3]
# 나온 결과값에 반복하여 실행되어 나온 결과값을 더하여 출력한다.    
    total_profit += total_profit

print(total_profit)

