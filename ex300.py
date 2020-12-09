#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]

for i in per:
#  try 코드를 사용하여 수행할 코드를 지정한다.  
    try:
        print(float(i))
# except 코드를 사용하여 예외가 발생했을 때 수행할 코드를 지정한다.    
    except:
        print(0)
# else 코드를 사용하여 예외가 발생하지 않았을 때 수행할 코드를 지정한다.
    else:
        print("clean data")
# finally 코드를 사용하여 예외 발생 여부와 상관없이 항상 수행할 코드를 지정한다.    
    finally:
        print("변환 완료")

