#!/usr/bin/env python
# coding: utf-8

# In[1]:


# fruit라는 이름의 dictionary를 생성한다.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# input함수의 인자에 출력하고 싶은 말을 넣으면 그것이 문자열로 반환된다.
user = input("좋아하는 과일은?")
# user가 fruit라는 dict의 values에 있을 경우 if문이 그대로 실행된다.
# "정답입니다." 가 출력된다.
if user in fruit.values():
    print("정답입니다.")
# if문이 실행되지 않을 경우 else문이 실행된다.
# "오답입니다." 가 출력된다.
else:
    print("오답입니다.")

