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
#        self.board=[1,3,0,4,8,2,7,6,5]
        self.n=n
    def toString(self):
        print(self.n)
        for i in range(1,self.n+1):
            print(self.board[self.n*(i-1):self.n*(i)])
    def hamming(self):
        global goal_board
        goal_board=[]
        for i in range(1,self.n*self.n):
            goal_board.append(i)
        goal_board.append(0)
        s=-1
        non_hamming=0
        for a in self.board:
            s+=1
            if a!=0:
                if a==goal_board[s]:
                    non_hamming+=1
        return abs((len(self.board)-1)-non_hamming)
    def manhattan(self):
        manhattan=0
        for a in self.board:
            if a!=0:
                if a==self.board.index(a)+1:
                    continue
                else:
                        index=self.board.index(a)
                        index_orginal=goal_board.index(a)
                        for i in range(1,self.n+1):
                            if a in self.board[self.n*(i-1):self.n*(i)]:
                                layer=i
                        for i in range(1,self.n+1):
                            if a in goal_board[self.n*(i-1):self.n*(i)]:
                                layer_orginal=i
                        layer_difference=layer-layer_orginal
                        if layer_difference==0:
                            manhattan+=(abs(index_orginal-index))
                        else:
                            if layer_difference>0:
                                index_score=index
                                for i in range(1,abs(layer_difference)+1):
                                    index_score=(index_score-self.n)
                                manhattan+=(abs(index_orginal-index_score)+abs(layer_difference))
                            else:
                                index_score=index
                                for i in range(1,abs(layer_difference)+1):
                                    index_score=(index_score+self.n)
                                manhattan+=(abs(index_orginal-index_score)+abs(layer_difference))
                
        return manhattan
    def neighbors(self):
         index=self.board.index(0)
         if index>0 and index<self.n:
            print(index)
            left=self.board[index-1]
            right=self.board[index+1]
            for i in range(1,self.n+1):
                if left in self.board[self.n*(i-1):self.n*(i)]:
                        layer_left_orgin=i
            for i in range(1,self.n+1):
                if right in self.board[self.n*(i-1):self.n*(i)]:
                        layer_right_orgin=i
            down=self.board[index+self.n]
            states_pos=[left,right,down]
            s=0
            for i in states_pos:
                s+=1
                if i==left:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_left_new=i
                    if layer_left_new-layer_left_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                elif i==right:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_right_new=i
                    if layer_right_new-layer_right_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                else:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    print("State {}".format(s))
                    for ii in range(1,self.n+1):
                        print(board_copy[self.n*(ii-1):self.n*(ii)])
                    
                    
         elif index>=((len(self.board)-1)-(self.n-1)) and index<len(self.board)-1:
            print(index)
            left=self.board[index-1]
            right=self.board[index+1]
            for i in range(1,self.n+1):
                if left in self.board[self.n*(i-1):self.n*(i)]:
                        layer_left_orgin=i
            for i in range(1,self.n+1):
                if right in self.board[self.n*(i-1):self.n*(i)]:
                        layer_right_orgin=i
                        
            up=self.board[index-self.n]
            states_pos=[left,right,up]
            s=0
            for i in states_pos:
                s+=1
                if i==left:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_left_new=i
                    if layer_left_new-layer_left_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                elif i==right:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_right_new=i
                    if layer_right_new-layer_right_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                else:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    print("State {}".format(s))
                    for ii in range(1,self.n+1):
                        print(board_copy[self.n*(ii-1):self.n*(ii)])
         elif index==0:
            print(index)
            right=self.board[index+1]
            for i in range(1,self.n+1):
                if right in self.board[self.n*(i-1):self.n*(i)]:
                        layer_right_orgin=i
            
            
            down=self.board[index+self.n]
            states_pos=[right,down]
            s=0
            for i in states_pos:
                s+=1
                if i==right:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_right_new=i
                    if layer_right_new-layer_right_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                else:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    print("State {}".format(s))
                    for ii in range(1,self.n+1):
                        print(board_copy[self.n*(ii-1):self.n*(ii)])
         elif index==len(self.board)-1:
            print(index)
            
            left=self.board[index-1]
            for i in range(1,self.n+1):
                    if left in self.board[self.n*(i-1):self.n*(i)]:
                        layer_left_orgin=i
                    
            up=self.board[index-self.n]
            states_pos=[up,left]
            s=0
            for i in states_pos:
                s+=1
                if i==left:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_left_new=i
                    if layer_left_new-layer_left_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                else:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    print("State {}".format(s))
                    for ii in range(1,self.n+1):
                        print(board_copy[self.n*(ii-1):self.n*(ii)])
        
         else:
            print(index)
            right,left=0,0
            up=self.board[index-self.n]
            down=self.board[index+self.n]
            try:
                left=self.board[index-1]
                for i in range(1,self.n+1):
                    if left in self.board[self.n*(i-1):self.n*(i)]:
                        layer_left_orgin=i
            except IndexError:
                states_pos=[right,up,down]
            try:
                right=self.board[index+1]
                for i in range(1,self.n+1):
                    if right in self.board[self.n*(i-1):self.n*(i)]:
                        layer_right_orgin=i
            except IndexError:
                states_pos=[left,up,down]
            
            states_pos=[left,right,up,down]
            s=0
            for i in states_pos:
                s+=1
                if i==left:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_left_new=i
                    if layer_left_new-layer_left_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                elif i==right:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    for i in range(1,self.n+1):
                         if board_copy[index] in board_copy[self.n*(i-1):self.n*(i)]:
                             layer_right_new=i
                    if layer_right_new-layer_right_orgin!=0:
                        s=s-1
                        continue
                    else:        
                        print("State {}".format(s))
                        for ii in range(1,self.n+1):
                            print(board_copy[self.n*(ii-1):self.n*(ii)])
                else:
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                    print("State {}".format(s))
                    for ii in range(1,self.n+1):
                        print(board_copy[self.n*(ii-1):self.n*(ii)])
                

        
       
   
board=Board([],6)
board.toString()
board.neighbors()



