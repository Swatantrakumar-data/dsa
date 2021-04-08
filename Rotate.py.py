#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class Linklist:
    def __init__(self):
        self.head = None
        
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def display(self):
        if self.head is None:
            print('list empty')
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()
        
        
    def rotate(self):
        p = self.head
        q = self.head
        prev = None
        
        while p.next is not None:
            prev = p
            p = p.next
            q = q.next
            
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None
        
        
        
    
        
x = Linklist()
x.append(10)
x.append(20)
x.append(30)
x.append(40)
x.display()
x.rotate()
x.display()


# In[ ]:




