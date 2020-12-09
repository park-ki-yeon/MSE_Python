#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import함수를 이용하여 numpy 모듈을 사용할수 있게 불러온다.
import numpy
# arrange 함수를 이용하여 step의 간격만큼 일정하게 떨어진 숫자들을 array형태로 
# 반환한다.
# for문을 이용하여 변수에 원소들을 대입하고 수행할 문장을 반복 실행한다.
for i in numpy.arange(0, 5, 0.1):
    print(i)

