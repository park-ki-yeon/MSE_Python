#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# icecream이라는 이름의 dictionary를 만들고 key는 '폴라포','빵빠레','월드콘,'메로나'
# 를 설정하고 value는 '1200','1800','1500','1000'을 대입해 반환한다.
>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream dictionary의 '누가바' key에 해당하는 value를 반환한다.
>> icecream['누가바']
# 딕셔너리에 없는 key를 사용하여 인덱싱했기 때문에 에러가 난다.
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'

