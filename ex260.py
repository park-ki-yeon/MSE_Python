#!/usr/bin/env python
# coding: utf-8

# In[4]:


class OMG : 
    def print() :
        print("Oh my god")

myStock = OMG() 
# print메서드를 호출한 객체가 ()안으로 넘어간다.
# 위의 def함수를 사용하여 함수를 지정한 부분에서 self가 없기 때문에 에러가 난다.
myStock.print()

