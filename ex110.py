#!/usr/bin/env python
# coding: utf-8

# In[1]:


# if 조건이 참이면 그대로 실행된다. 조건은 참이므로 실행된다.
if True :
# if 조건이 참이면 그대로 실행된다. 조건이 거짓이므로 실행되지 않는다.   
    if False:
        print("1")
        print("2")
# if false문이 실행되지 않으므로 else문이 실행된다.
# 3이 출력된다. 
    else:
        print("3")
# if문이 실행되지 않을때는 else문을 실행한다.
# print함수를 사용해서 4를 출력한다.
# if 조건이 참이여서 if문이 실행되므로 else문은 실행되지 않는다.
else :
    print("4")
# print함수를 사용해서 5를 출력한다.
print("5")

