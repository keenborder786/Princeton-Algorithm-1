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
    line_segment=[]
    result=[]
    for orgin in lists:
        segment=[]
        segment.append((None,(orgin.point[0],orgin.point[1])))
        gradients=[]
        for q in lists:
            if q!=orgin:
                grad=orgin.slopTo(q.point[0],q.point[1])
                gradients.append([grad,(q.point[0],q.point[1])])
        gradients=sorted(gradients)
        s=0
        for grad in gradients:
            if s==0:
                segment.append((grad[0],grad[1]))
                prev_grad=grad
                s+=1
            elif prev_grad[0]==grad[0] and prev_grad[1] not in segment and segment[-1][0]==grad[0]:
                segment.append((grad[0],grad[1]))
                segment.append((grad[0],prev_grad[1]))
            elif prev_grad[0]==grad[0] and segment[-1][0]==grad[0]:
                 segment.append((grad[0],grad[1]))
            else:
                if len(segment)>=3:
                    line_segment.append(list(set(segment)))
                    segment=[]
                    segment.append((grad[0],grad[1]))
                else:
                    segment=[]
                    segment.append((grad[0],grad[1]))
            prev_grad=grad
    for i in line_segment:
        draw=[]
        for k in i:
            draw.append(k[1])
            draw=sorted(draw)
        if len(draw)>=4:
            result.append(draw)
    print(result)
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    s=0
    final_result=[]
    for draw in result:
            if draw not in final_result:
                final_result.append(draw)
           
            
    time_end=time.time()
    return final_result,(time_end-time_start)
                
            
            
                   
           

if __name__=='__main__':
    k=Point(1,3)
    l=Point(2,6)
    m=Point(3,9)
    x=Point(4,12)
    a=Point(1,1)
    b=Point(2,2)
    c=Point(3,3)
    d=Point(4,4)
    q=Point(1,4)
    w=Point(2,8)
    e=Point(3,12)
    r=Point(4,16)
    t=Point(5,20)
    y=Point(6,24)
    u=Point(1,5)
    i=Point(4,4)
    
    FCP,times=FastCollinearPoints([k,l,m,x,a,b,c,d,q,w,e,r,t,y,u,i])
    print("The output of FastCollinearPoints Algorithm is {} and time taken is {}".format(FCP,times))
    BCP,times= BruteCollinearPoints([k,l,m,x,a,b,c,d,q,w,e,r,t,y,u,i])
    print("The output of BruteCollinearPoints Algorithm is {} and time taken is {}".format(BCP,times))