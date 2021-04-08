#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self,data=None,Next=None):
        self.data = data
        self.Next = Next
        
class Linklist:
    def __init__(self):
        self.head = None
        
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.Next is not None:
            last_node = last_node.Next
        
        last_node.Next = new_node
            
            
        
    def Has_Loop(self):
        if self.find_cycle() is None:
            return False
        else:
            return True
    
    def Find_Loop(self):
        if (self.start is None) or (self.Next is None):
            return None
        
        first_loop = self.start
        second_loop = self.start
        while (second_loop is not None) and (second_loop.Next is not None):
            first_loop = first_loop.Next
            second_loop = second_loop.Next.Next
            if first_loop == second_loop:
                return first_loop
        return None

