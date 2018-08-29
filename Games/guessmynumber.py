#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:12:31 2017

@author: alyshahelenic
"""

low = 0
high = 100
ans = 50

print('Please think of a number between 1 and 100!')
print('Is your secret number ' + str(int(ans)) + '?')
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
user = input()
while user:
    if user == 'l':
        low = int(ans)
        ans = (high + low)/2
        print('Is your secret number ' + str(int(ans)) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
        user = input()
    elif user == 'h':
        high = int(ans)
        ans = (high + low)/2
        print('Is your secret number ' + str(int(ans)) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
        user = input()
    elif user == 'c':
        print('Game over. Your secret number was: ' + str(int(ans)) + '.')
        break
    elif user != 'l' or user != 'c' or user != 'h':
        print("I'm sorry, I didn't understand that input.")
        print('Is your secret number ' + str(int(ans)) + '?')
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.", end = ' ')
        user = input()