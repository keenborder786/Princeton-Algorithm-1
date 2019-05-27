# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:14:51 2019

@author: MMOHTASHIM
"""
class quickfindUF(object):
    def __init__(self,ids):
        self.ids=ids
    def boolean_connected(self,p,q):
        return self.ids[p]==self.ids[q]
    def union(self,p,q):
        p_id=self.ids[p]
        for i in range(0,len(self.ids)):
            if self.ids[i]==p_id:
                self.ids[q]=p_id



class quickUnion(object):
    def __init__(self,ids):
        self.ids=ids
    def initiation(self):
        for i in range(0,len(self.ids)):
            self.ids[i]=i  
    def find_root(self,i):
        while i!=self.ids[i]:
            i=self.ids[i]
        return i
    def boolean_connected(self,p,q):
        return self.find_root(p)==self.find_root(q)
    def union(self,p,q):
        p_id=self.find_root(p)
        q_id=self.find_root(q)
        self.ids[p_id]=q_id



        