# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:40:32 2019

@author: MMOHTASHIM
"""
class Node(object):
    def __init__(self,d,n=None):
        self.data=d
        self.next_node=n
    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node=n
    def get_data(self):
        return self.data

class Linked_List(object):
    def __init__(self,r=None):
       self.root=r
       if r.get_next()!= None:
            self.last=Node(r.get_next().get_data())
            self.size=2
       else:
            self.last=self.root
            self.size=1
    def get_size(self):
        return self.size
    def find_last(self):
        return self.last
    def add(self,d):##Now we will add to the last
        old_last=self.find_last()
        old_last.set_next(d)
        self.last=Node(d,None)
    def remove(self,d): 
        this_node=self.root
        prev_node=None
        while this_node:
            if this_node.get_data()==d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root=this_node
                    
                self.size-=1
                return True
            else:
                prev_node=this_node 
                this_node=this_node.get_next()
        return False
    def pop(self):##stack implemenation-same implementation in both slack and queue
        this_node=self.root
        next_node=this_node.get_next
        self.root=next_node
    def find(self,d):
        this_node=self.root
        while this_node:
            if this_node.get_data()==d:
                return d
            else:
                this_node=this_node.get_next()
        return None
    
            

