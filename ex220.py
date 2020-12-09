#!/usr/bin/env python
# coding: utf-8

# In[3]:


# def함수를 이용하여 함수를 정의한다.
def print_max(a, b, c) :
# 함수의 값을 지정한다.    
    max_val = 0
# if문을 이용하여 조건이 참이면 다음 수행할 문장을 실행한다.    
   if a > max_val :
        max_val = a
# if문을 이용하여 조건이 참이면 다음 수행할 문장을 실행한다.  
    if b > max_val :
        max_val = b
# if문을 이용하여 조건이 참이면 다음 수행할 문장을 실행한다.    
    if c > max_val :
        max_val = c
# print함수를 이용하여 max_val의 값을 출력한다.    
    print(max_val)

print_max(10,20,30)

