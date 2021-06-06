#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from boardparams import *
import random

def drop_piece(board, row, selection, piece):
    board[row][selection] = piece
    return np.int_(board)

def is_column_empty(board, selection):
    if board[ROW_COUNT-1][selection] == 0:
        return True
    
def get_next_open_row(board, selection):
    for row in range(ROW_COUNT):
        if board[row][selection] == 0:
            return row
        
def has_player_won(board, piece):
    #Horizontal win
    for window in horizontal_windows:
        if board[window[0]] == piece:
            if board[window[1]] == piece:
                if board[window[2]] == piece:
                    if board[window[3]] == piece:
                        return True
    
    #Vertical win                    
    for window in vertical_windows:
        if board[window[0]] == piece:
            if board[window[1]] == piece:
                if board[window[2]] == piece:
                    if board[window[3]] == piece:
                        return True
                    
    #Positively sloping diagonal win                     
    for window in pos_diag_windows:
        if board[window[0]] == piece:
            if board[window[1]] == piece:
                if board[window[2]] == piece:
                    if board[window[3]] == piece:
                        return True
                        
    #Negatively sloping diagonal win           
    for window in neg_diag_windows:
        if board[window[0]] == piece:
            if board[window[1]] == piece:
                if board[window[2]] == piece:
                    if board[window[3]] == piece:
                        return True

def create_board():
    board = np.zeros((6,7))
    return np.int_(board)

def action_space(board):
    possible_actions = []
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][column] == 0:
                possible_actions.append((row,column))
                break
    return possible_actions

def random_bot(board):
    selection = random.choice(action_space(board))[1]
    return selection

def blocker_bot(board, BOT):
    if BOT == 1:
        opp_piece == 2
    else:
        opp_piece == 1
    for row, column in action_space(board):
        pass
    


# In[ ]:


foo = [1,2]
BOT = None
HUMAN_PLAYER = random.choice(foo)
if HUMAN_PLAYER == 1:
    BOT = 2
else:
    BOT = 1
print(f"LET'S PLAY CONNECT FOUR!!")
print(f"You play: player {HUMAN_PLAYER},\nBOT plays: player {BOT} ")

board = create_board()
print(np.flip(board,0))
turn = 0
game_over = False


while not game_over:
    turn +=1
    if turn >= COLUMN_COUNT*ROW_COUNT:
        print(np.flip(board,0))
        print(f"Game Drawn")
        break
    else:
        print(f"Turn {turn}, game is in progress...")
        if turn % 2 == 1:
            piece = 1
        else:
            piece = 2
            
    if piece == HUMAN_PLAYER:    
        selection = input(f"Player {piece} make your selection [0-6] or press 'q' to QUIT") 

        while not selection in str([0,1,2,3,4,5,6,'q']):
            selection = input(f"Invalid input. Player {piece} make your selection [0-6] or press 'q' to QUIT")
        if selection == 'q':
            print("exiting...")
            break
        else:
            selection = int(selection)

        while not is_column_empty(board, selection):
            selection = input(f"Player {piece} pick a different column or press 'q' to QUIT") 
            while not selection in str([0,1,2,3,4,5,6,'q']):
                selection = input(f"Invalid input. Player {piece} make your selection [0-6] or press 'q' to QUIT")
            if selection == 'q':
                break
            else:
                selection = int(selection)
        if selection == 'q':
            print("exiting...")
            break

        row = get_next_open_row(board, selection)
        drop_piece(board, row, selection, piece)
        game_over = has_player_won(board, piece)
        print(np.flip(board,0))
        

        if game_over:
            print(f"Game Over! Player {piece} wins!") 
            print(np.flip(board,0))
            break
            
    elif piece == BOT:    
        selection = random_bot(board)
        row = get_next_open_row(board, selection)
        drop_piece(board, row, selection, piece)
        game_over = has_player_won(board, piece)
        print(np.flip(board,0))
        print(f"random bot chose column {selection}")

        if game_over:
            print(f"Game Over! Player {piece} wins!") 
            print(np.flip(board,0))
            break

