#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data라는 이름의 list를 작성한다. 원소는 '09/05', '09/06', '09/07', '09/08', '09/09'
# 대입하여 생성한다.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price라는 이름의 list를 작성한다. 원소는 10500, 10300, 10100, 10800, 11000
# 를 대입하여 생성한다.
close_price = [10500, 10300, 10100, 10800, 11000]
# close_table이라는 변수값을 zip함수와 dict함수를 이용하여 dictionary로 반환한다.
# zip함수를 사용하여 동일한 개수로 이루어진 자료형을 쌍을 지어 묶어준다.
# dict함수를 사용하여 생성된 자료형을 dictionary로 변환하여 생성한다.
close_table = dict(zip(date, close_price))
# close_table 의 값을 print함수를 사용하여 출력한다.
print(close_table)

