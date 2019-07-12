# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:31:36 2019

@author: MMOHTASHIM
"""

import numpy as np
import random
#alpha stage
class Board(object):
    def __init__(self,board,n):
        for i in range(n*n):
            board.append(i)
        self.board=random.sample(board, len(board))   
        self.n=n
    def toString(self):
        print(self.n)
        for i in range(1,self.n+1):
            print(self.board[self.n*(i-1):self.n*(i)])
    def hamming(self):
        goal_board=[]
        for i in range(self.n*self.n):
            goal_board.append(i)
        s=-1
        hamming=0
        for a in self.board:
            s+=1
            if a==goal_board[s]:
                hamming+=1
        return hamming
    def manhattan(self):
        goal_board=[]
        for i in range(self.n*self.n):
            goal_board.append(i)
        manhattan=0
        for a in self.board:
            if a==self.board.index(a)+1:
                continue
            elif a==0:
                if self.board.index(a)+1==len(self.board):
                    continue
                else:
                    index=self.board.index(a)
                    print("index",index)
                    for i in range(1,self.n+1):
                        if a in self.board[self.n*(i-1):self.n*(i)]:
                            layer=i
                    layer_difference=layer-self.n
                    print("layer_difference",layer_difference)
                    if layer_difference==0:
                        manhattan+=(abs(len(self.board)-index))-1
                    else:
                        if layer_difference>0:
                            index_score=index
                            for i in range(1,abs(layer_difference)+1):
                                index_score=(index_score-self.n)
                            print(index_score)
                            manhattan=((abs(len(self.board)-1)-index_score)+abs(layer_difference))
                        else:
                            index_score=index
                            for i in range(1,abs(layer_difference)+1):
                                index_score=(index_score+self.n)
                            print(index_score)
                            manhattan=(((len(self.board)-1)-index_score)+abs(layer_difference))
            else:
                continue###rest of code(same implementation as above but some differences)
        return manhattan
        

        
       
        
board=Board([],4)
board.toString()
print(board.manhattan())