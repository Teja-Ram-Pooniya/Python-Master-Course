# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 23:03:17 2023

@author: Teja Ram Pooniya
@Program: Game-Programming in Python

@Description:
    using loops in a simple text-based tic-tac-toe game in Python:
        This simple tic-tac-toe game uses a 3x3 board and 
        allows two players (X and O) to take turns entering their moves. 
        The game continues until there is a winner or a draw. It's a fun
        way to explore loops, conditional statements, and two-dimensional 
        lists in Python.
"""

# Initialize the tic-tac-toe board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to display the current state of the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Game loop
current_player = 'X'
while True:
    display_board()
    row = int(input(f"Player {current_player}, enter row (0-2): "))
    col = int(input(f"Player {current_player}, enter column (0-2): "))
    
    if board[row][col] == ' ':
        board[row][col] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print("Cell already occupied! Try again.")
    
    # Check for a win condition
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ' or \
           board[0][0] == board[1][1] == board[2][2] != ' ' or \
           board[0][2] == board[1][1] == board[2][0] != ' ':
            display_board()
            print(f"Player {current_player} wins!")
            break
    else:
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            display_board()
            print("It's a draw!")
            break
