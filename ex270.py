#!/usr/bin/env python
# coding: utf-8

# In[ ]:


종목 = []
# Stock클래스의 객체를 생성한다.
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
# append함수를 이용하여 list에 객체를 넣은다음 반환한다.
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
# i가 Stock클래스의 객체를 바인딩하므로 code와 per에 접근하여 그 값을 반환하여 출력한다.
for i in 종목:
    print(i.code, i.per)

