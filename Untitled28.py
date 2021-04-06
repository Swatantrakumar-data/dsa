#!/usr/bin/env python
# coding: utf-8

# In[17]:


def sub_list(l):
    l1 = []
    list = [l1]
    for i in range(len(l)):
        old_list = list[:]
        new_list = l[i]
        for j in range(len(list)):
            list[j] = list[j] + [new_list]
        list = old_list + list
    return list

l = [2,7,5]
print(sub_list(l)[1:])
    


# In[ ]:




