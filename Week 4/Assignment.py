# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:31:36 2019

@author: MMOHTASHIM
"""

import numpy as np
import random
def goal_unsolvables(n):
    goalies_board=[i for i in range(1,n*n)]
    goalies_board.append(0)
    possibilies=[]
    
    for i in goalies_board:
        if i!=0:
            index_now=goalies_board.index(i)
        for ii in range(0,len(goalies_board)):
            if index_now!=ii and ii!=(len(goalies_board)-1):
                goalies_board_copy=goalies_board.copy()
                value=goalies_board_copy[index_now]
                goalies_board_copy[index_now]=goalies_board_copy[ii]
                goalies_board_copy[ii]=value
                possibilies.append(goalies_board_copy)
    return possibilies

#alpha stage
class Board(object):
    def __init__(self,board,n):
        self.board=board
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
        global goal_board
        goal_board=[]
        for i in range(1,self.n*self.n):
            goal_board.append(i)
        goal_board.append(0)
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
         neighbors=[]
         index=self.board.index(0)
         if index>0 and index<self.n:
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
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                neighbors.append(board_copy)
                    
                    
         elif index>=((len(self.board)-1)-(self.n-1)) and index<len(self.board)-1:
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
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                        
                neighbors.append(board_copy)
         elif index==0:
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
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                neighbors.append(board_copy)
                
                
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
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                neighbors.append(board_copy)
        
         else:
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
            
            s=0
            states_pos=[left,right,up,down]
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
                    board_copy=self.board.copy()
                    pos_index=board_copy.index(i)
                    board_copy[pos_index]=0
                    board_copy[index]=i
                

                neighbors.append(board_copy)
         return neighbors

class AI(object):
    def __init__(self):
        self.moves=0
    def Solver(self,board):
        goal_unsolvable=goal_unsolvables(board.n)
        game_on=True
        n=board.n
        ##intialize the solver
        goalies_board=[i for i in range(1,n*n)]
        goalies_board.append(0)
        neighbors=board.neighbors()
        self.moves+=1
        l=0
        pq=[]
        board_deleted=[]
        while game_on==True:
            print("#############################################################################################")
            a=0
            for i in neighbors:
                a+=1
                if i==goalies_board:
                    game_on=False
                    print("The solution reached in {} moves".format(self.moves) ,"and the solution is",i)
                if i in goal_unsolvable:
                    game_on=False
                    print("The solution is unsolvable")
                if i not in pq and i not in board_deleted :
                    pq.append(i)
            min_pq=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            min_pq_tie=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            for i in pq[-a:]:###using cache mathana value instead of recomputing it when requeing the values
                board=Board(i,n)
                man=board.manhattan()
                ham=board.hamming()
                if board.manhattan()<min_pq:
                    min_pq=man
                    del_board=i
                elif man==min_pq:
                    if ham<min_pq_tie:
                        min_pq_tie=ham
                        del_board=i
            print(pq[-a:])
                    
            neighbors=Board(del_board,n).neighbors()###critical optimization 1 to Algorithm
            for i in neighbors:
                if i==board:
                    neighbors.remove(i)
            board=del_board
            
            pq.remove(del_board)
            board_deleted.append(del_board)
            self.moves+=1
     
            
            

                   
                
                
                    
        
        
        
            
                
                

        
       
if __name__=="__main__": 
    n=3
    puzzle=[2,1,0,7,8,5,4,3,6]
    board=Board(puzzle,n)
    board.toString()
    solve=AI()
    solve.Solver(board)
    



