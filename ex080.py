#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data 변수값을 range함수를 사용하여 list로 반환한다. 
# range 함수는 (시작값, 끝나는값, 수를 증가시키는 간격)을 이용하여 원소들을 
# list로 반환한다. 끝나는 값은 list에 포함되지 않는다.
# 생성된 list를 tuple함수를 사용하여 tuple로 변환하여 생성한다.
data = tuple(range(2, 100, 2))
# 변환되어진 data 변수값을 print함수를 사용하여 출력한다. 
print( data )

