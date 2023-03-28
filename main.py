#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:21:47 2021

@author: aadilshaikh
"""

import subprocess

print("\n        Hello")

while True:
    ch = int(input("\tMenu\n\n1: Play Game\n2: Instructions\n3: Creaters\n4: Exit\n\nYour Choice - "))
    print()
    
    if ch==1:
        cmd = 'python Home.py'
        p = subprocess.Popen(cmd, shell = True)
        p.communicate

    
    elif ch==2:
        print("\tGENERAL INSTRUCTIONS\n")
        print("The main objective of the game is to reach the opposite end of the diagonal.")
        print("There are 3 different levels.")
        print("The rest of the levels are unlocked only when the previous one is completed.")
        print("Your score will the time you take to finish the game.\n\n")
        print("\tGAME INSTRUCTIONS\n")
        print("When you land on a block it's colour will change.")
        print("RED colour indicates the block will BREAK in 2 seconds.")
        print("GREEN colour indicates the block will not break.")
        print("You need to jump on every ORANGE coloured check point.")
        print("Failure to do this will not let you complete the level.")
        
    elif ch==3:
        print("Created By :\tAadil Shaikh")
    
    elif ch==4:
        print("\nThank You")
        break 
    
    else:
        print("Please choose a option from the Menu :)")



