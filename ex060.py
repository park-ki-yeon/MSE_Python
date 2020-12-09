#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 이름이 nums인 list함수를 작성하고 원소 1, 2, 3, 4, 5를 대입하여 생성한다.
nums = [1, 2, 3, 4, 5]
# sum함수와 len함수를 사용하여 list의 평균값을 계산하고 반환한다.
# sum함수는 list원소들의 합을 계산하여 반환하고 len함수는 list원소들의 개수를 반환
#한다.
average = sum(nums) / len(nums)
# average 변수값을 print함수를 사용하여 출력한다.
print(average)

