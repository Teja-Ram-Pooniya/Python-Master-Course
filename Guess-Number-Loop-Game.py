# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 22:53:03 2023

@author: Teja Ram Pooniya
@Program: Topic - Loops - Guess a number Game Buil with the help of loops in 
                            in python programming developer.

@Description:   Let's take a simple example of a guessing game using loops in Python. 
                In this game, the player has to guess a randomly generated number, 
                and the game provides hints if the guess is too high or too low.

"""
# importing the random library packege for unique random number generator.
import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Game loop
while True:
    # Get player's guess
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Compare guess with target number
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop when the correct number is guessed

"""
The game starts with generating a random number. 
The player's guess is then compared to the target number using an if-elif-else structure. 
If the guess is too low or too high, the player is given a hint, 
and they are prompted to guess again. If the guess is correct, 
the game congratulates the player and the loop is exited using break.

This simple game demonstrates the use of loops to repeatedly prompt the player 
for guesses until the correct number is guessed. You can build more 
complex games using similar loop and conditional structures along with 
other Python features.
"""
