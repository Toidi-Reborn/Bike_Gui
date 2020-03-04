from tkinter import *
from tkinter import ttk
from random import *
import time
import random
from PIL import Image, ImageTk




testmode = True




class frameSetUp:
    eRow = {}
    dRow = {}
    cRow = {}
    bRow = {}
    aRow = {}
    wSet = {}
    speed = 0

    def __init__(self):
        tHeight = screenH * 0.90
        self.tFrame = Frame(gui, height=tHeight)
        self.bFrame = Frame(gui, bg='red')
        self.tFrame.grid(row=0, column=0, sticky='nesw')
        self.bFrame.grid(row=1, column=0, sticky='nesw')
        Grid.columnconfigure(gui, 0, weight=1)
        Grid.rowconfigure(gui, 0, weight=1)
    
        self.setFrameBoxes()
        self.clockRun()
        
        if testmode == True:
            self.rTest()
        
    def getTime(self):
        now = time.localtime(time.time())
        timeM = " AM"
        timeHour = now.tm_hour
        if timeHour > 12:
            timeHour = now.tm_hour - 12
            timeM = " PM"
        timeMin = now.tm_min
        if timeMin < 10:
            timeMin = "0" + str(now.tm_min)
        timeSec = now.tm_sec
        if timeSec < 10:
            timeSec = "0" + str(now.tm_sec)
        now = str(now.tm_mon) + "/" + str(now.tm_mday) + "/" + str(now.tm_year) + " " + str(timeHour) + ":" + str(
            timeMin) + ":" + str(timeSec) + str(timeM)
        return now


    def clockRun(self):
        x = self.getTime()
        self.lTime.config(text=x)
        gui.after(1000, self.clockRun)


    def rTest(self):
        x = randint(0,10)
        #self.l1.config(text=x)
        #self.l2.config(text=x*234)

        gpsDir = ['North', 'East', 'South', 'West']
        self.dir.config(text=random.choice(gpsDir))

        nTurn = ['Straight', 'Left', 'Right', 'U-Turn']
        self.b5.config(text=random.choice(nTurn))

        gearList = ['N', '1', '2', '3','4','5','6']         ### For testing
        gChoice = random.choice(gearList)
        self.gear.config(text=gChoice)
        if gChoice == "N":
            self.gear.config(bg="green")
        else:
            self.gear.config(bg="grey")


        self.speed = randint(0,120)    ### For testing speed
        needleA = 135 - (self.speed * 2.25)
        self.speedNeedle2 = ImageTk.PhotoImage(self.speedNeedle.rotate(needleA))
        self.cImg2 = self.canvas.create_image(self.canvasW/2,self.canvasH/2, image = self.speedNeedle2)


        self.barSpeed['value'] = abs(self.speed)        
        self.speedNumber.config(text=abs(self.speed))
        
        rpm = randint(5000, 18000)         ### For testing
        self.barRPM['value'] = rpm

        if rpm > 10000:
            self.barRPMNumber.config(bg="red", text=rpm)
        else:
            self.barRPMNumber.config(bg="white", text=rpm)
        
        self.temp1.config(text=randint(20,150))
        self.temp2.config(text=randint(20,150))
        self.temp3.config(text=randint(20,150))
        self.temp4.config(text=randint(20,150))

        self.temp1I.config(text=randint(20,150))
        self.temp2I.config(text=randint(20,150))
        self.temp3I.config(text=randint(20,150))
        self.temp4I.config(text=randint(20,150))
        gui.after(250, self.rTest)
        
        
    def setFrameBoxes(self):

        self.aRow[0] = StringVar()
        self.aRow[0] = Frame(self.tFrame)
        self.aRow[0].grid(row=0, column=0, columnspan=5)
        self.lTime = Label(self.aRow[0], font=("", 30))
        self.lTime.grid(row=0, column=0)


        self.wSet = Frame(self.tFrame, width=1000)
        self.wSet.grid(row=1, column=0, columnspan=5)


        for i in range(0,5):
            self.bRow[i] = StringVar()
            self.bRow[i] = Frame(self.tFrame)
            self.bRow[i].grid(row=2, column=i)
            self.cRow[i] = StringVar()
            self.cRow[i] = Frame(self.tFrame, width=12)
            self.cRow[i].grid(row=3, column=i)
            self.dRow[i] = StringVar()
            self.dRow[i] = Frame(self.tFrame)
            self.dRow[i].grid(row=4, column=i)
            self.eRow[i] = StringVar()
            self.eRow[i] = Frame(self.tFrame)
            self.eRow[i].grid(row=5, column=i)
            if i == 3:
                self.eRow[i].grid(columnspan=2)
                self.dRow[i].grid(columnspan=2)


        ###  Navigation
        self.b1 = Label(self.bRow[0], text="")
        self.b1.grid(row=0, column=0)

        self.b2 = Label(self.bRow[1], text="Current Road", font=("", 30))
        self.b2.grid(row=0, column=0)

        self.dir = Label(self.bRow[2], text="Direction", font=("", 30), padx=20, width=7)
        self.dir.grid(row=0, column=0)

        self.b4 = Label(self.bRow[3], text="Dn", font=("", 30))
        self.b4.grid(row=0, column=0)

        self.b5 = Label(self.bRow[4], text="Next", font=("", 30), width=7, anchor=N)
        self.b5.grid(row=0, column=0)
        self.b6 = Label(self.bRow[4], text="Next road", font=("", 30), width=20, anchor=W)
        self.b6.grid(row=0, column=1)


        ######  Temps

        self.temp1 = Label(self.cRow[0], text='Engine Temp 1: ', anchor=W)
        self.temp1.grid(row=0, column=0, sticky="nesw")
        self.temp2 = Label(self.cRow[0], text='Engine Temp 2: ', anchor=W)
        self.temp2.grid(row=1, column=0, sticky="nesw")
        self.temp3 = Label(self.cRow[0], text='Engine Temp 3: ', anchor=W)
        self.temp3.grid(row=2, column=0, sticky="nesw")
        self.temp4 = Label(self.cRow[0], text='Engine Temp 4: ', anchor=W)
        self.temp4.grid(row=3, column=0, sticky="nesw")

        self.temp1 = Label(self.cRow[0], anchor=E, width=3)
        self.temp1.grid(row=0, column=1, sticky="nesw")
        self.temp2 = Label(self.cRow[0], anchor=E, width=3)
        self.temp2.grid(row=1, column=1, sticky="nesw")
        self.temp3 = Label(self.cRow[0], anchor=E, width=3)
        self.temp3.grid(row=2, column=1, sticky="nesw")
        self.temp4 = Label(self.cRow[0], anchor=E, width=3)
        self.temp4.grid(row=3, column=1, sticky="nesw")

        self.temp1It = Label(self.cRow[1], text='Intake Temp 1: ', anchor=W)
        self.temp1It.grid(row=0, column=0, sticky="nesw")
        self.temp2It = Label(self.cRow[1], text='Intake Temp 2: ', anchor=W)
        self.temp2It.grid(row=1, column=0, sticky="nesw")
        self.temp3It = Label(self.cRow[1], text='Intake Temp 3: ', anchor=W)
        self.temp3It.grid(row=2, column=0, sticky="nesw")
        self.temp4It = Label(self.cRow[1], text='Intake Temp 4: ', anchor=W)
        self.temp4It.grid(row=3, column=0, sticky="nesw")

        self.temp1I = Label(self.cRow[1], anchor=E, width=3)
        self.temp1I.grid(row=0, column=1, sticky="nesw")
        self.temp2I = Label(self.cRow[1], anchor=E, width=3)
        self.temp2I.grid(row=1, column=1, sticky="nesw")
        self.temp3I = Label(self.cRow[1], anchor=E, width=3)
        self.temp3I.grid(row=2, column=1, sticky="nesw")
        self.temp4I = Label(self.cRow[1], anchor=E, width=3)
        self.temp4I.grid(row=3, column=1, sticky="nesw")

        self.m1 = Label(self.cRow[2], text='?? 1: ', anchor=W)
        self.m1.grid(row=0, column=0, sticky="nesw")
        self.m2 = Label(self.cRow[2], text='?? 2: ', anchor=W)
        self.m2.grid(row=1, column=0, sticky="nesw")
        self.m3 = Label(self.cRow[2], text='?? 3: ', anchor=W)
        self.m3.grid(row=2, column=0, sticky="nesw")
        self.m4 = Label(self.cRow[2], text='?? 4: ', anchor=W)
        self.m4.grid(row=3, column=0, sticky="nesw")

        self.m1 = Label(self.cRow[2], anchor=E, width=3)
        self.m1.grid(row=0, column=1, sticky="nesw")
        self.m2 = Label(self.cRow[2], anchor=E, width=3)
        self.m2.grid(row=1, column=1, sticky="nesw")
        self.m3 = Label(self.cRow[2], anchor=E, width=3)
        self.m3.grid(row=2, column=1, sticky="nesw")
        self.m4 = Label(self.cRow[2], anchor=E, width=3)
        self.m4.grid(row=3, column=1, sticky="nesw")



        for i in range(3):
            for child in self.cRow[i].winfo_children():
                child.config(font=("",20))
         
        ######  RPM
        """
        self.dRow[3] = StringVar()
        self.dRow[3] = Frame(self.tFrame)
        self.dRow[3].grid(row=5, column=3, rowspan=1, columnspan=2, sticky='nesw') 
        """     
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", troughcolor='Red', background='Green')
        self.barSpeed = ttk.Progressbar(self.dRow[3], style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, maximum=100)
        self.barSpeed.grid(row=0, column=0, padx=10, pady=10, ipady=10)
        self.barSpeed['value'] = 0

        self.barRPM = ttk.Progressbar(self.dRow[3], style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, maximum=18000)
        self.barRPM.grid(row=1, column=0, padx=10, pady=10, ipady=10)
        self.barRPM['value'] = 0
        self.barRPMNumber = Label(self.dRow[3], text="23432", font=("System", 30))
        self.barRPMNumber.grid(row=2, column=0, columnspan=2, sticky='nesw')





        ##### Gear
        self.eRow[0].config(relief='sunken')
        self.gear = Label(self.eRow[0], font=('System',75), text='fdf', relief='solid')
        self.gear.grid(row=0, column=0, sticky='nesw')
        
        self.speedNumber = Label(self.eRow[1], text="speed", font=("System", 40))
        self.speedNumber.grid(row=0, column=0, sticky='nesw')
        Label(self.eRow[1], text="MPH").grid(row=1, column=0, sticky=N)
        Label(self.eRow[2], text="MPH").grid(row=1, column=0, sticky=N)
    
        
        for i in range(0,4):
            Label(self.dRow[i], text="HHHHHHHHHHHHH").grid(row=0, column=0, sticky='nesw')
        
        ### Speed Image

        ## MATH!!!!!!!
        ## 0mph = 135    160 mph= -225
        ## 360 / 160 = 2.25 per MPH

        self.speedB = Image.open('index/speedBackT.png')
        self.speedNeedle = Image.open('index/needleT.png')
        self.speedB2 = ImageTk.PhotoImage(self.speedB)
        self.canvasW = self.speedB2.width()
        self.canvasH = self.speedB2.height()

        self.canvas = Canvas(self.eRow[3], width=self.canvasW, height=self.canvasH)
        self.canvas.grid(row=0, column=0)
        self.cImg = self.canvas.create_image(self.canvasW/2,self.canvasH/2, image = self.speedB2)

        '''
        create_arc(bbox, options)
        create_bitmap(position, options)
        create_image(position, options)
        create_line(coords, options)
        create_oval(bbox, options)
        create_polygon(coords, options)
        create_rectangle(bbox, options)
        create_text(position, options)
        create_window(position, options)
        '''


        frameList = [self.aRow, self.bRow, self.dRow, self.eRow]

        for i in frameList:
            for each in i:
                Grid.rowconfigure(i[each], 0, weight=1)
                Grid.columnconfigure(i[each], 0, weight=1)
       
        size = self.tFrame.grid_size()

        for i in range(size[0]):
            Grid.columnconfigure(self.tFrame, i, weight=1)
        for i in range(size[1]):
            Grid.rowconfigure(self.tFrame, i, weight=1)


gui = Tk()
gui.title("Bike")
#base.wm_attributes('-transparentcolor', 'black')

screenHP = gui.winfo_screenheight()
screenWP = gui.winfo_screenwidth()

screenH = screenHP - 1000
screenW = screenWP - 1000

cRowWidth = screenW / 5

#gui.geometry('%dx%d+%d+%d' % (screenW, screenH, 50, 50))
frameSetUp()
gui.mainloop()
