# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:13:41 2019

@author: MMOHTASHIM
"""
##In Progress

##Point Class to represent a single point on a 2-D plane
class point2d(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def double_x(self):
        return self.x
    def double_y(self):
        return self.y
    def distanceto(self,point):
        return (((self.x-point.x)**2)+((self.y-point.y)**2))**(1/2)
    def distancetoSquare(self,point):
        return (self.distanceto(point))**2
    def compareTo(self,point):
        if self.y>point.y:
            return (self.x,self.y)
        elif point.y>self.y:
            return(point.x,point.y)
        else:
            if self.x>point.x:
                return (self.x,self.y)
            elif point.x>self.x:
                return (point.x,point.y)
    def equals(self,point):
        if self.x==point.x and self.y==point.y:
            return True
        else:
            return False
##A Rectangle class to represent a A 2-D rectangle on the same 2-D plane as for point class.
class RectHV(object):
    def __init__(self,xmin,xmax,ymin,ymax):
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
    def xmin(self):
        return self.xmin
    def xmax(self):
        return self.xmax
    def ymin(self):
        return self.ymin
    def ymax(self):
        return self.ymax
    def contains(self,point):
        if point.x>=self.xmin and point.x<=self.xmax:
            if point.y>=self.ymin and point.y<=self.ymax:
                return True
            else:
                return False
        else:
            return False
    def intersects(self,Rect):
        points=[point2d(Rect.xmin,Rect.ymin),point2d(Rect.xmax,Rect.ymin),point2d(Rect.xmin,Rect.ymax),point2d(Rect.xmax,Rect.ymax)]
        for i in points:
            if self.contains(i):
                return True
    def distanceto(self,p):
        if p.y>=self.ymin and p.y<=self.ymax:
            dist1=p.distanceto(point2d(self.xmax,p.y))
            dist2=p.distanceto(point2d(self.xmin,p.y))
            return min([dist1,dist2])
        elif p.x>=self.xmin and p.x<=self.max:    
            dist3=p.distanceto(point2d(p.x,self.ymax))
            dist4=p.distanceto(point2d(p.x,self.ymin))
            return min([dist3,dist4])
        else:
            dist5=p.distanceto(point2d(self.xmin,self.ymin))
            dist6=p.distanceto(point2d(self.xmax,self.ymin))
            dist7=p.distanceto(point2d(self.xmin,self.ymax))
            dist8=p.distanceto(point2d(self.xmax,self.ymax))
            return min([dist5,dist6,dist7,dist8])
    def distanceSquaredTo(self,p):
        return (self.distanceSquaredTo(p))**2
    def equal(self,rect):
        if self.xmin==rect.xmin and self.xmax==rect.xmax and self.ymax==rect.ymax and self.ymin==rect.ymin:
            return True
        else:
            return False
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if '__main__' == __name__:
    point=point2d(0.7,0.4)
    rect=RectHV(0.7,0.9,0.1,0.3)
    rect1=RectHV(0.7,0.9,0.1,0.3)

            