# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:43:34 2019

@author: MMOHTASHIM
"""
###Basic idea of stack(Last in first out(LIFO))
def stack(lists,a='-'):
    stack=[]
    for i in lists:
        if i==a:
            print(stack.pop())
        else:
            stack.append(i)
###Linked List-stack implementation
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
        self.size=0
    def get_size(self):
        return self.size
    def add(self,d):
        new_node=Node(d,self.root)
        self.root=new_node
        self.size+=1
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
    def pop(self):##stack implemenation
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
    
class stack_array_implementation(object):#stack overflow when N>capcity,using capcity as cheat in this simple implmenation
    def __init__(self,arr,capcity):
        self.arr=arr
        self.capcity=capcity
        self.n=(len(self.arr)-1)
    def push(self,n):
        self.arr[self.n]=n
        self.n+=1
    def pop(self,n):
        del self.arr[self.n-1]
        self.n-=1


class resize_array(object):
    def __init__(self,arr):
        self.arr=arr
        self.N=len([i for i in arr if i!= None])
        self.capcity=len(arr)
    def push(self,a):
        self.capcity=len(self.arr)
        self.N=len([s for s in self.arr if s!= None])
        if self.N==self.capcity:
            for i in range(self.N):
                if i==0:
                    self.arr.append(a)
                else:
                    self.arr.append(None)
        else:
           self.arr[self.N]=a
        self.capcity=len(self.arr)
        self.N=len([s for s in self.arr if s!= None])
    def pop(self,a):
        if self.N==len(self.arr)/4:
            self.arr=self.arr[:(len(self.arr))/2]
            self.arr.pop(a)
        else:
            self.arr.pop(a)
            
            


     
            
            
            
            
            
            
            


            
        



        
    
        
    