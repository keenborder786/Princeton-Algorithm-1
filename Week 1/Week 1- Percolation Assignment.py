# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:31:39 2019

@author: MMOHTASHIM
"""

import random
from statistics import mean,stdev

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
#            self.ids[i]=self.ids[self.ids[i]]###this is only difference in code as compare to previous one,as we are flattening out our binary tree
            i=self.ids[i]
        return i
    def boolean_connected(self,p,q):
        return self.find_root(p)==self.find_root(q)
    def union(self,p,q):
        p_id=self.find_root(p)
        q_id=self.find_root(q)
        if self.wieghts[p_id]<self.wieghts[q_id]:
            self.ids[p_id]=q_id
            self.wieghts[q_id]+=self.wieghts[p_id]
        else:
            self.ids[q_id]=p_id
            self.wieghts[p_id]+=self.wieghts[q_id]


def MonteCarloSimulation(n,T):
    grid_size=n*n### T is the number of trials
    grid=[]
    grid_oc=[]
    grid_wieght=[]
    probs=[]
    for i in range(grid_size):
        grid.append(i)
        grid_oc.append(0)###at first all spots are closed
        grid_wieght.append(1)
    graph=flattenedweightagequickUnion(grid,grid_wieght)

    
    for t in range(T):
        index=random.randint(0,len(grid_oc)-1)
        grid_oc[index]=1
        up=0
        right=0
        left=0
        down=0
#        print(index)
        roots=[]
        roots_u=[]
#        print(graph.ids)
        
        if index<n*2 and index>n:
            left=grid_oc[index-1]
            right=grid_oc[index+1]
            up=grid_oc[index-n]
            down=grid_oc[index+n]
        elif index>0 and index<n:
            left=grid_oc[index-1]
            right=grid_oc[index+1]
            down=grid_oc[index+n]
        elif index>n*2 and index<len(grid_oc)-1:
            up=grid_oc[index-n]
            left=grid_oc[index-1]
            right=grid_oc[index+1]
        elif index==0:
            right=grid_oc[index+1]
            down=grid_oc[index+n]
        elif index==len(grid_oc)-1:
            left=grid_oc[index-1]
            up=grid_oc[index-n]
        if left==1:
            p=graph.ids[index]
            q=graph.ids[left]
            graph.union(p,q)
        if right==1:
            p=graph.ids[index]
            q=graph.ids[right]
            graph.union(p,q)
        if up==1:
            p=graph.ids[index]
            q=graph.ids[up]
            graph.union(p,q)
        if down==1:
            p=graph.ids[index]
            q=graph.ids[down]
            graph.union(p,q)
        for i in range(n):
           root=graph.find_root(i)
           roots.append(root)
        for i in range(n*2,n*n):
           root=graph.find_root(i)
           roots_u.append(root)
        if bool(set(roots) & set(roots_u)):
            opens=grid_oc.count(1)
            total=len(grid_oc)
            prob=opens/total
            probs.append(prob)
    return (mean(probs),"confidence=+-",1.96*stdev(probs))    
               
                    
        
print(MonteCarloSimulation(100,24000))
    
    
    
    