# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:14:51 2019

@author: MMOHTASHIM
"""
##These are three different methods of union and each one is an improvement on the last one to improve the time complexity of each 
#algorithm as compare to the last one
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
        
class weightagequickUnion(object):
    def __init__(self,ids,wieghts):
        self.ids=ids
        self.wieghts=wieghts
    def initiation(self):
        for i in range(0,len(self.ids)):
            self.ids[i]=i 
        for i in range(len(self.wieghts)):
            self.wieghts[i]=1
    def find_root(self,i):
        while i!=self.ids[i]:
            i=self.ids[i]
        return i
    def union(self,p,q):
        p_id=self.find_root(p)
        q_id=self.find_root(q)
        if self.wieghts[p_id]<self.wieghts[q_id]:
            self.ids[p_id]=q_id
            self.wieghts[q_id]+=self.wieghts[p_id]
        else:
            self.ids[q_id]=p_id
            self.wieghts[p_id]+=self.wieghts[q_id]

class flattenedweightagequickUnion(object):
    def __init__(self,ids,wieghts):
        self.ids=ids
        self.wieghts=wieghts
    def initiation(self):
        for i in range(0,len(self.ids)):
            self.ids[i]=i 
        for i in range(len(self.wieghts)):
            self.wieghts[i]=1
    def find_root(self,i):
        while i!=self.ids[i]:
            self.ids[i]=self.ids[self.ids[i]]###this is only difference in code as compare to previous one,as we are flattening out our binary tree
            i=self.ids[i]
        return i
    def union(self,p,q):
        p_id=self.find_root(p)
        q_id=self.find_root(q)
        if self.wieghts[p_id]<self.wieghts[q_id]:
            self.ids[p_id]=q_id
            self.wieghts[q_id]+=self.wieghts[p_id]
        else:
            self.ids[q_id]=p_id
            self.wieghts[p_id]+=self.wieghts[q_id]


  
###Below is an application of quick find in which I try to find the timestamp at which all memebers are somehow related to each other
class SocialNetwork(object):
    def __init__(self,ids,sz,t):
        self.ids=ids
        self.sz=sz
        self.t=0
    def initiation(self):
        for i in range(len(self.ids)):
            self.ids[i]=i
        for i in range(len(self.sz)):
            self.sz[i]=1
    def find_root(self,i):
        while i!=self.ids[i]:
            i=self.ids[i]
        return i
    def connected(self,p,q):
        return self.find_root(p)==self.find_root(q)
    def union(self,p,q):
        p_id=self.find_root(p)
        q_id=self.find_root(q)
        if self.sz[q_id]<self.sz[p_id]:
            self.ids[q_id]=p_id
            self.sz[p_id]+=self.sz[q_id]
            self.t+=1
        else:
            self.ids[p_id]=q_id
            self.sz[q_id]+=self.sz[p_id]
            self.t+=1
    def find(self,i):
        lst=[]
        for p in range(len(self.ids)):
            if self.connected(i,p):
                lst.append(p)
        return max(lst)
    def Successor(self,x):
        self.union(x,x+1)
        sucessors=self.find(x)
        return sucessors
        


graph=SocialNetwork([0,1,2,3,4,5],[2,2,2,2,2,2],0)
graph.initiation()
print(graph.ids)
graph.union(4,5)
graph.union(5,0)
print(graph.ids)
print(graph.Successor(3))
print(graph.ids)


        


        
        

        