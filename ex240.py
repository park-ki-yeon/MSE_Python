#!/usr/bin/env python
# coding: utf-8

# In[1]:


# def함수를 이용하여 함수를 지정한다.
# num이라는 변수에 대입된 숫자에 2를 곱하여 반환한다.
def 함수0(num) :
    return num * 2
# def함수를 이용하여 함수를 지정한다.
# 함수0의 num변수에 2를 더하여 반환한다.
def 함수1(num) :
    return 함수0(num + 2)
# def함수를 이용하여 함수를 지정한다.
# num이라는 변수에 10을 더한후 다시 num 변수에 바인딩하여 반환한다.
# 반환된 값을 함수1의 num변수에 대입하여 반환한다.
def 함수2(num) :
    num = num + 10
    return 함수1(num)
# print함수를 이용하여 함수2(2)값을 출력한다.
c = 함수2(2)
print(c)

