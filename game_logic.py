#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from boardparams import *

def drop_piece(board, row, selection, piece):
    board[row][selection] = piece
    return board

def is_column_empty(board, selection):
    if board[ROW_COUNT-1][selection] == 0:
        return True
    
def get_next_open_row(board, selection):
    for row in range(ROW_COUNT):
        if board[row][selection] == 0:
            return row
        
def win_condition(board, piece):
    for c in range(COLUMN_COUNT-4):
        for r in range(ROW_COUNT-4):
            #Horizontal win
            if board[r][c] == piece:
                if board[r][c+1] == piece:
                    if board[r][c+2] == piece:
                        if board[r][c+3] == piece:
                            return True
            #Vertical win
                elif board[r+1][c] == piece:
                    if board[r+2][c] == piece:
                        if board[r+3][c] == piece:
                            return True
                            
            #Positively sloping diagonal win
                elif board[r+1][c+1] == piece:
                    if board[r+2][c+2] == piece:
                        if board[r+3][c+3] == piece:
                            return True
                        
            #Negatively sloping diagonal win           
    for c in range(COLUMN_COUNT-3,COLUMN_COUNT):
        for r in range(ROW_COUNT-3):    
            if board[r][c] == piece:
                if board[r+1][c-1] == piece:
                    if board[r+2][c-2] == piece:
                        if board[r+3][c-3] == piece:
                            return True

def create_board():
    board = np.zeros((6,7))
    return board
    
game_over = False
board = create_board()
turn = 0

while not game_over:
    turn +=1
    if turn >= COLUMN_COUNT*ROW_COUNT:
        print(f"Game Drawn")  
        break
    else:
        if turn % 2 == 1:
            piece = 1
        else:
            piece = 2
        selection = int(input(f"Player {piece} make your selection"))
        while not is_column_empty(board, selection):
            selection = int(input(f"Player {piece} pick a different column"))
        row = get_next_open_row(board, selection)
        drop_piece(board, row, selection, piece)
        game_over = win_condition(board, piece)
        if game_over:
            print(f"Game Over! Player {piece} wins!") 
            print(np.flip(board,0))
            break
    print(np.flip(board,0))

