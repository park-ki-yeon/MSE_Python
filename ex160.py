#!/usr/bin/env python
# coding: utf-8

# In[7]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
# 변수를 split함수를 이용하여 문자열을 특정 구분자로 나누어서 반환한다.
# 반환되어 나온 값을 split이라는 변수로 지정한다.
  split = 변수.split(".")
# if조건이 참이면 수행될 문장을 실행한다.
# 논리연산자 or를 사용하여 두조건중 하나만 충족되도 수행될 문장이 실행된다.
  if (split[1] == "h") or (split[1] == "c"):
        print(변수)

