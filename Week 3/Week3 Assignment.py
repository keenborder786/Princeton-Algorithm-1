# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:51:02 2019

@author: MMOHTASHIM
"""
from itertools import combinations
import matplotlib.pyplot as plt
import time
import math
class Point():
    def __init__(self,x,y):
        self.point=(x,y)
        self.line_segment=[]
    def draw_point(self):
        plt.scatter(self.point[0],self.point[1])
    def draw_line_segment(self,x0,y0):
        plt.plot([self.point[0],x0],[self.point[1],y0])
        self.line_segment.append((x0,y0))
    def compareto(self,x0,y0):
        if y0<self.point[1]:
            return True
        if y0==self.point[1]:
            if x0<self.point[0]:
                return True
        return False
    def slopTo(self,x0,y0):
        if x0==self.point[0] and y0==self.point[1]:
            return -(math.inf)
        elif y0==self.point[1]:
            return 0
        elif  x0==self.point[0]:
            return -(math.inf)
        gradient=(self.point[1]-y0)/(self.point[0]-x0)
        return gradient
    def slopeOrder(self,point1,point2):
        gradient_1=self.slopTo(point1[0],point1[1])
        gradient_2=self.slopTo(point2[0],point2[1])
        if  gradient_1>gradient_2:
            return point1
        else:
            return point2
##A brute force algorithm to check for collinearity of the points
def BruteCollinearPoints(lists):
    time_start=time.time()
    combination_list=list(set(combinations(lists,4)))
    result=[]
    for pair in  combination_list:
        p=pair[0]
        q=pair[1]
        r=pair[2]
        s=pair[3]
        g1=p.slopTo(q.point[0],q.point[1])
        g2=p.slopTo(r.point[0],r.point[1])
        g3=p.slopTo(s.point[0],s.point[1])
        if g1==g2==g3:
            result.append([(p.point[0],p.point[1]),(q.point[0],q.point[1]),(r.point[0],r.point[1])
            ,(s.point[0],s.point[1])])
    time_end=time.time()
    return result,(time_end-time_start)

def FastCollinearPoints(lists):
    time_start=time.time()
    orgin=lists[0]
    gradients=[]
    line_segment=[]
    for q in lists:
        if q!=orgin:
            grad=orgin.slopTo(q.point[0],q.point[1])
            gradients.append([grad,(q.point[0],q.point[1])])
    gradients=sorted(gradients)
    adjacent=None
    for grads in gradients:
        if adjacent==None:
            adjacent=grads
        else:
            if grads[0]==adjacent[0]:
                line_segment.append(grads[1])
                line_segment.append(adjacent[1])
        adjacent=grads
    if len(line_segment)>=3:
        time_end=time.time()
        return sorted(list(set(line_segment))),(time_end-time_start)
    return None,(time_end-time_start)
                
            
            
                   
           

if __name__=='__main__':
    a=Point(1,1)
    b=Point(2,2)
    c=Point(3,3)
    d=Point(4,4)
    e=Point(4,4)
    f=Point(5,5)
    g=Point(6,6)
    h=Point(45,45)
    j=Point(113,1)
    k=Point(2,2313)
    l=Point(3,333)
    m=Point(444,4)
    
    FCP,times=FastCollinearPoints([a,b,c,d,e,f,g,h,j,k,l,m])
    BCP,times= BruteCollinearPoints([a,b,c,d,e,f,g,h,j,k,l,m])
    print("The output of FastCollinearPoints Algorithm is {} and time taken is {}".format(FCP,times))
    print("The output of BruteCollinearPoints Algorithm is {} and time taken is {}".format(BCP,times))