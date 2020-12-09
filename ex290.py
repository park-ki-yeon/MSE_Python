#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 부모class의 객체를 생성하고 생성자를 만든다.
# 생성자가 호출되면 부모생성을 출력한다.
class 부모:
  def __init__(self):
    print("부모생성")
# 자식 class의 객체를 생성하고 생성자를 만든다.
# 생성자가 호출되면 자식생성을 출력한다.
# super 키워드를 사용해 부모class에 접근할수 있도록 한다.
class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

