#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:06:00 2021

@author: aadilshaikh
"""

import mysql.connector as connector
import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Checkbutton
import subprocess
global UserInfo

info = []

def toggle_password():
    if myEntryPass.cget('show') == '':
        myEntryPass.config(show='*')
    else:
        myEntryPass.config(show='')

def SignUp():

    myWindow=tk.Tk()
    myWindow.title("Add Log")
    myWindow.geometry("600x300")
    
    myLabelTitle = Label(myWindow,text="CREATE AN ACCOUNT !!",padx=75,pady=15,bg='blue',fg='White',font=('times',30))
    myLabelTitle.place(x=0,y=20,width=600,height=50)
    
    myLabelName=Label(myWindow,text="Name",padx=75,pady=15,font=('times',20))
    myLabelName.place(x=175,y=100,width=100,height=25)
    
    myEntryName = Entry(myWindow,width=35) #Name Input
    myEntryName.place(x=275,y=100,width=150,height=25)
    
    myLabelID = Label(myWindow,text="UserID",padx=75,pady=15,font=('times',20)) #User ID Title
    myLabelID.place(x=175,y=150,width=100,height=25)
    
    myEntryID = Entry(myWindow,width=35) #User ID Input
    myEntryID.place(x=275,y=150,width=150,height=25)
    
    myLabelPass = Label(myWindow,text="Password",padx=75,pady=15,font=('times',20)) #User ID Title
    myLabelPass.place(x=175,y=200,width=100,height=25)
    
    myEntryPass = Entry(myWindow,width=35) #User ID Input
    myEntryPass.place(x=275,y=200,width=150,height=25)
    
    myButtonSubmit = Button(myWindow,text="Submit",padx=20,pady=10,command = lambda:AddData(myWindow,myEntryName,myEntryID,myEntryPass))#Add command
    myButtonSubmit.place(x=455,y=230,width=125,height=50)
    
    
def AddData(myWindow,myEntryName,myEntryID,myEntryPass):  
    
    info=[myEntryName.get(),myEntryID.get(),myEntryPass.get(),1,32767,32767,32767]
    info = tuple(info)
    mycon=connector.connect(host='localhost', user='root', passwd='istanbul2005', database='podar12_21')
    if mycon.is_connected==False:
        print("Error connecting to database:")
    else:
        myQry="INSERT INTO PlayerData VALUES(%s,%s,%s,%s,%s,%s,%s)"            
        myCursor=mycon.cursor()       
        try:
            myCursor.execute(myQry,info)
            mycon.commit()
            mycon.close()
            myWindow.destroy()                
        except:
            myLabelID = Label(myWindow,text="Already Taken",padx=75,pady=15,font=('times',15))
            myLabelID.place(x=450,y=150,width=125,height=25)
            
        
def MainGame(myEntryID,myEntryPass,myWindow):
    
    global UserInfo
    mycon=connector.connect(host='localhost', user='root', passwd='istanbul2005', database='podar12_21')
    if mycon.is_connected==False:
        print("Error connecting to database:")
    else:
        myQry = "SELECT * FROM PlayerData where User_ID = %s and Password = %s"
        myCursor=mycon.cursor()
        myCursor.execute(myQry,(myEntryID.get(),myEntryPass.get()))       
        UserInfo=myCursor.fetchone()
        mycon.close()
        
        
        if myCursor.rowcount!= -1:
            with open ("player.txt","w") as myfile:
                myfile.write(UserInfo[1]+"~"+UserInfo[2])
            
            myWindowGame=tk.Tk()
            myWindowGame.title("WELCOME")
            myWindowGame.geometry("600x600")
            
            myLabelTitle = Label(myWindowGame,text="!! SKY-BLOCK 3000 !!",padx=75,pady=15,bg='blue',fg='White',font=('times',30))
            myLabelTitle.place(x=0,y=20,width=600,height=50)
            
            myLabelName=Label(myWindowGame,text=UserInfo[0],padx=75,pady=15,font=('times',20))
            myLabelName.place(x=225,y=100,width=150,height=25)
            
            myLabelHighScore=Label(myWindowGame,text="HighScore: "+str(UserInfo[4]),padx=75,pady=15,font=('times',20)) 
            myLabelHighScore.place(x=300,y=150,width=200,height=100)
            
            myLabelHighScore=Label(myWindowGame,text="HighScore: "+str(UserInfo[5]),padx=75,pady=15,font=('times',20)) 
            myLabelHighScore.place(x=300,y=300,width=200,height=100)
    
            myLabelHighScore=Label(myWindowGame,text="HighScore: "+str(UserInfo[6]),padx=75,pady=15,font=('times',20)) 
            myLabelHighScore.place(x=300,y=450,width=200,height=100)
            
                   
            myButtonlvl1 = Button(myWindowGame,text="LEVEL I",padx=75,pady=15,font=('times',30),command = Level_I) 
            myButtonlvl1.place(x=50,y=150,width=200,height=100)
            
            if UserInfo[3] > 1: #Check for level
                myButtonlvl2 = Button(myWindowGame,text="LEVEL II",padx=75,pady=15,font=('times',30),command = Level_II) 
                myButtonlvl2.place(x=50,y=300,width=200,height=100)
            else:
                myButtonlvl2 = Button(myWindowGame,text="LEVEL II",padx=75,pady=15,font=('times',30),command = Level_II,state="disabled") 
                myButtonlvl2.place(x=50,y=300,width=200,height=100)
                
            if UserInfo[3] > 2: #Check for level
                myButtonlvl3 = Button(myWindowGame,text="LEVEL III",padx=75,pady=15,font=('times',30),command = Level_III) 
                myButtonlvl3.place(x=50,y=450,width=200,height=100)
            else:
                myButtonlvl3 = Button(myWindowGame,text="LEVEL III",padx=75,pady=15,font=('times',30),command = Level_III,state="disabled") 
                myButtonlvl3.place(x=50,y=450,width=200,height=100)
            
            
            myWindow.destroy()
        
      
      
        else:
            myLabelIncorrect = Label(myWindow,text="Incorrect UserID or Password",padx=75,pady=15,font=('times',15)) #User ID Title
            myLabelIncorrect.place(x=0,y=200,width=600,height=25)
  
        
def Level_I():
    cmd = 'python Level_I.py'
    p = subprocess.Popen(cmd, shell = True)
    p.communicate()

  
def Level_II():
    cmd = 'python Level_II.py'
    p = subprocess.Popen(cmd, shell = True)
    p.communicate()


def Level_III():
    cmd = 'python Level_III.py'
    p = subprocess.Popen(cmd, shell = True)
    p.communicate()

    


myWindow=tk.Tk()
myWindow.title("Sky-Block 3000")
myWindow.geometry("600x300")

myLabelTitle = Label(myWindow,text="LOGIN",padx=75,pady=15,bg='blue',fg='White',font=('times',30))
myLabelTitle.place(x=0,y=20,width=600,height=50)

myLabelID = Label(myWindow,text="UserID",padx=75,pady=15,font=('times',20)) #User ID Title
myLabelID.place(x=175,y=100,width=100,height=25)

myEntryID = Entry(myWindow,width=35) #User ID Input
myEntryID.place(x=275,y=100,width=150,height=25)

myLabelPass = Label(myWindow,text="Password",padx=75,pady=15,font=('times',20)) #User ID Title
myLabelPass.place(x=175,y=150,width=100,height=25)

myEntryPass = Entry(myWindow,width=35,show="*") #Password ID Input
myEntryPass.place(x=275,y=150,width=150,height=25)

myCheckPass = Checkbutton(text=" Show",font=('times',15),command = toggle_password)
myCheckPass.place(x=445,y=150,width=70,height=25)

myButtonSignIn = Button(myWindow,text="Sign in",padx=20,pady=10,command = lambda:MainGame(myEntryID,myEntryPass,myWindow))#Add command
myButtonSignIn.place(x=455,y=230,width=125,height=50)

myButtonSignUp = Button(myWindow,text="Sign up",padx=20,pady=10,command = SignUp)#Add command
myButtonSignUp.place(x=30,y=230,width=125,height=50)
  
myWindow.mainloop()
