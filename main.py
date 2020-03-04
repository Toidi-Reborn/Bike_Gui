import socket
import sqlite3
from tkinter import *
import requests
import telnetlib
import datetime
from datetime import datetime
from PIL import Image, ImageTk
from phue import Bridge
import random


lightConnect = False



class myWindow:
    def __init__(self):
        Grid.rowconfigure(base, 1, weight=1)
        Grid.columnconfigure(base, 0, weight=1)
        self.topFrame = Frame(base, bg='yellow')          
        self.midFrame = Frame(base, bg="red")
        self.bottomFrame = Frame(base)

        self.topFrame.grid(row=0, column=0, sticky="nesw")
        self.midFrame.grid(row=1, column=0, sticky="nesw")
        self.bottomFrame.grid(row=2, column=0, sticky="nesw")

        #Grid.columnconfigure(self.midFrame, 0, weight=1)
        #Grid.rowconfigure(self.midFrame, 0, weight=1)

        ####  Temp ---- just to fill space

        self.time = Label(self.topFrame, text="TOPPER - Title")
        self.time.grid(row=0, column=0)

        ### end temp

        self.mainFrame = Frame(self.midFrame, bg='blue')
        self.gpsFrame = Frame(self.midFrame)
        self.lightFrame = Frame(self.midFrame)
        self.setBottomButton()

        self.lightSetUp()
        self.getTime()
        self.dashBoardSetUp()


    def getTime(self):
        now = datetime.now()
        now = now.strftime('%I:%M:%S %p')
        self.time.configure(text=now)
        base.after(1000, self.getTime)

    dashFrame = []
    dashLabel = []


    def dashBoardSetUp(self):
        for i in range(6):
            self.dashFrame.append(Frame(self.mainFrame, bg="green"))
            self.dashFrame[i].grid(row=0, column=i, sticky="nesw", pady=5, padx=5)
            self.dashLabel.append(Label(self.dashFrame[i], text=i))
            self.dashLabel[i].grid(row=0, column=0) 
        for i in range(6):
            Grid.columnconfigure(self.midFrame, i, weight=1)    



        '''
        dashFrame[0] = Frame(self.midFrame, relief='solid')
        dashFrame[0].grid(row=0, column=0)
        dashFrame[1] = Frame(self.midFrame, relief='solid')
        dashFrame[1].grid(row=0, column=1)
        dashFrame[2] = Frame(self.midFrame, relief='solid')
        dashFrame[2].grid(row=0, column=2)
        dashFrame[3] = Frame(self.midFrame, relief='solid')
        dashFrame[3].grid(row=0, column=3)
        '''
        


    def setBottomButton(self):
        self.bOne = Button(self.bottomFrame, text="Dash Board", width=10, height=5, command = lambda x = self.mainFrame, y = "bOne": self.setWindow(y, x))
        self.bTwo = Button(self.bottomFrame, text="GPS", width=10, height=5, command = lambda x = self.gpsFrame, y = "bTwo": self.setWindow(y, x))
        self.bThree = Button(self.bottomFrame, text="Lights", width=10, height=5, command = lambda x = self.lightFrame, y = "bFour": self.setWindow(y, x))
        self.bOne.grid(row=0, column=0, sticky='nesw')
        self.bTwo.grid(row=0, column=1, sticky='nesw')
        self.bThree.grid(row=0, column=2, sticky='nesw')
        for x in range(3):
            Grid.columnconfigure(self.bottomFrame, x, weight=1)  #each column will resize with change



    def setWindow(self, bt, win):
        for child in self.bottomFrame.winfo_children():
            child.configure(bg="white", fg="black")

        for child in self.midFrame.winfo_children():
            child.grid_forget()
        if bt == "bOne":
            self.bOne.configure(bg="black", fg="white")
        elif bt == "bTwo":
            self.bTwo.configure(bg="black", fg="white")
        elif bt == "bThree":
            self.bThree.configure(bg="black", fg="white")
        else:
            print("OOOOOOOOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHHHHHHHH        NNNNNNNNNNNNNOOOOOOOOOOOOOO")
             
        win.grid(row=0, column=0, sticky="nesw")

        
        ### get size of midFrame - column/row
        gridSize = win.grid_size()
        totalCol = gridSize[0]
        totalRows = gridSize[1]

        print(totalCol, totalRows)

        for x in range(totalCol):
            Grid.columnconfigure(win, x, weight=1)
        for x in range(totalRows):
            Grid.rowconfigure(win, x, weight=1)
        

    def lightSetUp(self):
        if lightConnect == False:
            print("Hue Light Connection Turned Off")
            Label(self.lightFrame, text="Light Connection was Disabled", font=("", 20)).grid(row=0, column=0)

        else:
            pass





base = Tk()
base.title("Phone App")
#base.wm_attributes('-transparentcolor', 'black')

screenHP = base.winfo_screenheight()
screenWP = base.winfo_screenwidth()
print(screenHP, screenWP)
screenH = 1080
screenW = 1720

base.geometry('%dx%d+%d+%d' % (screenW, screenH, 50, 50))

myWindow()
base.mainloop()






