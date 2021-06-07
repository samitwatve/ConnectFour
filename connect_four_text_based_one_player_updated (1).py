#!/usr/bin/env python
# coding: utf-8

# # Connect Four - single player

# Import packages

# In[ ]:


import numpy as np
from boardparams import *
import random


# ### Defining some useful functions

# Creates an empty board of sizes specified by `ROW_COUNT` and `COLUMN_COUNT` and fills each spot with zeroes. All zeroes get converted to ints before returning the board.

# In[ ]:


def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return np.int_(board)


# Takes the board and a selection (or column) as input and checks if the top row of the selected column is empty. If it is empty, then this function will return `True`, otherwise it will return `None`.

# In[ ]:


def is_column_empty(board, selection):
    if board[ROW_COUNT-1][selection] == 0:
        return True


# Takes the board and a selection (or column) as input and returns the lower-most row in that column. This is where the piece will drop due to gravity on a physical board.

# In[ ]:


def get_next_open_row(board, selection):
    for row in range(ROW_COUNT):
        if board[row][selection] == 0:
            return row


# Takes the board, row, selection (or column) and piece and places the piece in that location.
# 
# *Note: This must be used in conjunction with get_next_open_row() to make sure the row specified is the lower-most in that column.*

# In[ ]:


def drop_piece(board, row, selection, piece):
    board[row][selection] = piece
    return np.int_(board)


# Goes through each window in `horizontal_windows`, `vertical_windows`, `pos_diagonal_windows` and `neg_diagonal_windows` to see if any window has all four of the same piece. If yes, the function returns `True`. The windows are calculated separately in boardparams.py.

# In[ ]:


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


# For a given board, returns a list of all `possible_actions` that can be taken for that board for the current player in the current move (i.e. it is forward looking for 1 ply)

# In[ ]:


def action_space(board):
    possible_actions = []
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][column] == 0:
                possible_actions.append((row,column))
                break
    return possible_actions


# `random_bot`picks randomly between the actions within the action_space for the current board

# In[ ]:


def random_bot(board):
    selection = random.choice(action_space(board))[1]
    return selection


# `random_blocker_bot` looks at all horizontal, vertical and diagonal windows that contains an opponent piece and picks randomly between these windows.

# In[ ]:


def random_blocker_bot(board, BOT):
    #Checks which piece is the opponent's piece
    opp_piece = None
    if BOT == 1:
        opp_piece = 2
    else:
        opp_piece = 1
    
    #Iterate through all windows
    possible_windows = []    
    for window in all_windows:
        #Iterate through all possible positions within a window
        for position in window:
            #if opponent piece is found within that window, store that window
            if board[position] == opp_piece:
                possible_windows.append(window)
                
    #Checks if the board is empty and it's the bot's turn to play first            
    if len(possible_windows) == 0:
        #Picks randomly if it's playing first
        selection = random.choice(action_space(board))[1]
        
    else:   
        #Creates a flat list of all possible windows
        flat_list = []
        for sublist in possible_windows:
            for item in sublist:
                flat_list.append(item)
                
        #Then short_lists actions based on what's immediately playable and plays that.
        
        #This short-listing is necessary because in many cases, there are several positions in
        #diagonal windows that appear within possible_windows, but are not immediately playable.
        #As the board gets more populated with opponent pieces the number of positions that are 
        #contained within possible windows increases dramatically, but only a few of them are
        #playable.
        short_listed_actions = []
        for i in flat_list:
            if i in action_space(board):
                short_listed_actions.append(i)
                
        #Picks a random action within the short listed actions
        selection = random.choice(short_listed_actions)[1]
   
    return selection


# Prints out a better formatted board using string formatting. The background colors are defined in boardparams.py and are ANSI color codes that are actually strings that are formatted a particular way when printing to console. 
# 
# Source code from: https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
# 
# modified to fit our needs.

# In[ ]:


def pretty_print_board(board):
    flipped_board = np.flipud(board)
    
    #prints column labels
    print(f"{RED_BG} 0 {RED_BG} 1 {RED_BG} 2 {RED_BG} 3 {RED_BG} 4 {RED_BG} 5 {RED_BG} 6 {COLOR_OFF}")
    
    #iterate through each 1-D array (or row) in the board
    for row in flipped_board:
        row_str = ""
        
        #For each location in row, change background color based on value at that location
        for location in row:
            if location == 1:
                row_str += YELLOW_BG + " 1 "
            elif location ==2:
                row_str +=BLUE_BG + " 2 "
            else:
                row_str +=PINK_BG+"   "

        print(row_str+COLOR_OFF)


# # Main Game Loop

# There are 3 ways in which the game can end. 
# 
# 1) **Either player 1 or 2 wins** (i.e. when connect-four is acheived)
# 
# 2) **Game is drawn** (this happens when the total number of turns exceeds the number of slots on the board, but nobody has won)
# 
# 3) **Human player chooses to quit the game**
# 
# The main game loop keeps running unless one of these 3 things happen

# In[ ]:


#Welcome message
print(f"{GREEN_BG} LET'S PLAY CONNECT FOUR!! {COLOR_OFF}")

#Assigns Player 1 or 2 randomly
foo = [1,2]
HUMAN_PLAYER = random.choice(foo)
BOT = None
if HUMAN_PLAYER == 1:
    BOT = 2
    print(f"player {YELLOW_BG} 1: HUMAN {COLOR_OFF}, \n player {BLUE_BG} 2: BOT {COLOR_OFF}")
else:
    BOT = 1
    print(f"player {YELLOW_BG} 1: BOT {COLOR_OFF}, \n player {BLUE_BG} 2: HUMAN {COLOR_OFF}")
    
#Creates an empty game board
board = create_board()
# print(np.flip(board,0))
pretty_print_board(board)
turn = 0
game_over = False

#keeps running until one of the 3 exit conditions takes place
while not game_over:
    turn +=1
    #Checks if total number of turns has exceeded the number of slots and breaks
    if turn >= COLUMN_COUNT*ROW_COUNT:
        pretty_print_board(board)
#         print(np.flip(board,0))
        print(f"Game Drawn")
        break
    #Otherwise keeps going    
    else:
        print(f"Turn {turn}, game is in progress...")
        #alternates between player 1 (piece = 1) and player 2 (piece = 2)
        if turn % 2 == 1:
            piece = 1
        else:
            piece = 2
    #Asks the human player to make a selection        
    if piece == HUMAN_PLAYER:    
        selection = input(f"Player {piece} make your selection [0-6] or press 'q' to QUIT") 
        
        #Checks for invalid input or escape character 'q' and breaks if 'q' is pressed
        while not selection in str([0,1,2,3,4,5,6,'q']):
            selection = input(f"Invalid input. Player {piece} make your selection [0-6] or press 'q' to QUIT")
        if selection == 'q':
            print("exiting...")
            break
        # When input is valid the selection (or column) is converted to int    
        else:
            selection = int(selection)
        #Checks if the selected column is empty and if it's not, keeps prompting the user to 
        #pick a column that is empty
        while not is_column_empty(board, selection):
            selection = input(f"Player {piece} pick a different column or press 'q' to QUIT") 
                
            #Checks for invalid input or escape character 'q' and breaks if 'q' is pressed
            while not selection in str([0,1,2,3,4,5,6,'q']):
                selection = input(f"Invalid input. Player {piece} make your selection [0-6] or press 'q' to QUIT")
            if selection == 'q':
                break
            else:
                selection = int(selection)
                
        #This code block is repeated because there are two while loops that must be exited
        if selection == 'q':
            print("exiting...")
            break
            
        #Gets the next open row in the column that was selected
        row = get_next_open_row(board, selection)
        #and drops that piece in that spot
        drop_piece(board, row, selection, piece)
        #checks if player has won
        game_over = has_player_won(board, piece)
#         print(np.flip(board,0))
        pretty_print_board(board)
        
        #Exits if player has won    
        if game_over:
            print(f"Game Over! Player {piece} wins!") 
#             print(np.flip(board,0))
            pretty_print_board(board)
            break
            
    elif piece == BOT:    
        #gets a column from the BOT
        selection = random_blocker_bot(board, piece)
        #Gets the next open row in the column that was selected
        row = get_next_open_row(board, selection)
        #and drops that piece in that spot
        drop_piece(board, row, selection, piece)
        #checks if player has won
        game_over = has_player_won(board, piece)
        pretty_print_board(board)
#         print(np.flip(board,0))
        print(f"random blocker bot chose column {selection}")
        #Exits if player has won   
        if game_over:
            print(f"Game Over! Player {piece} wins!") 
#             print(np.flip(board,0))
            pretty_print_board(board)
            break

