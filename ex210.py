#!/usr/bin/env python
# coding: utf-8

# In[1]:


# def함수를 이용하여 함수를 정의한다.
# A를 출력한다.
def message1():
    print("A")
# def함수를 이용하여 함수를 정의한다.
# B를 출력한다.
def message2():
    print("B")
# def함수를 이용하여 함수를 정의한다.
def message3():
# for문을 이용하여 변수에 요소들을 대입하며 수행할 문장을 반복한다.
# 총 세번 반복하여 실행한다.
    for i in range (3) :
# message2를 출력한다.        
        message2()
# C를 출력한다.        
        print("C")
# for문의 반복 실행이 끝나고 message1를 출력한다.    
    message1()

message3()

