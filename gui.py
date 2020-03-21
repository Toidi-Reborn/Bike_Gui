from tkinter import *
from tkinter import ttk
from random import *
import time
import random
from PIL import Image, ImageTk

testmode = True
gpsOn = True
redLine = 14000


class frameSetUp:
    eRow = {}
    dRow = {}
    cRow = {}
    bRow = {}
    aRow = {}
    wSet = {}
    speed = 0
    rpm = 0
    speedUp = 0
    curGear = "N"

    def __init__(self):
        tHeight = screenH * 0.90
        self.tFrame = Frame(gui, height=tHeight)
        #self.bFrame = Frame(gui)
        self.tFrame.grid(row=0, column=0, sticky='nesw')
        #self.bFrame.grid(row=1, column=0, sticky='nesw')
        Grid.columnconfigure(gui, 0, weight=1)
        Grid.rowconfigure(gui, 0, weight=1)
    
        self.setFrameBoxes()
        self.clockRun()
        self.imageSet()

        for child in gui.winfo_children():
            child.config(bg="black")
            for child2 in child.winfo_children():
                for child3 in child2.winfo_children():
                    try:
                        child3.config(bg="black", fg="white")
                        child3.grid(sticky="nesw")
                    except:
                        pass

        if testmode:
            self.rTest()
        else:
            self.update()


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


    def imageSet(self):
        self.gN = Image.open('index/gear/gN.png')
        self.g1 = Image.open('index/gear/g1.png')
        self.g2 = Image.open('index/gear/g2.png')
        self.g3 = Image.open('index/gear/g3.png')
        self.g4 = Image.open('index/gear/g4.png')
        self.g5 = Image.open('index/gear/g5.png')        
        self.g6 = Image.open('index/gear/g6.png')        
        self.leftA = Image.open('index/arrowLT.png')        
        self.rightA = Image.open('index/gear/g6.png')
        self.gN = ImageTk.PhotoImage(self.gN)
        self.g1 = ImageTk.PhotoImage(self.g1)
        self.g2 = ImageTk.PhotoImage(self.g2)
        self.g3 = ImageTk.PhotoImage(self.g3)
        self.g4 = ImageTk.PhotoImage(self.g4)
        self.g5 = ImageTk.PhotoImage(self.g5)
        self.g6 = ImageTk.PhotoImage(self.g6)

        one = 100   #Gear position
        self.gNImage = self.canvasG.create_image(one, one+20, state="hidden", image = self.gN)
        self.g1Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g1)
        self.g2Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g2)
        self.g3Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g3)
        self.g4Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g4)
        self.g5Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g5)
        self.g6Image = self.canvasG.create_image(one, one+20, state="hidden", image = self.g6)


        
        self.gearList = [self.gNImage, self.g1Image, self.g2Image, self.g3Image, self.g4Image, self.g5Image, self.g6Image] 



    def update(self):
        arrowLOn = False
        arrowROn = False
        brake = False
        clutch = True
        rpm = 1432
        speed = 97
        needleA = 135 - (speed * 2.25)     # 360 - 90 = 270   270/120 = 2.25
        needleB = 135 - (rpm * 0.015)    #360 - 90 = 270    270/18000 = 0.015
        gear = self.gNImage
        turn = "Right"
        direction = "North"
        temp1 = 123
        temp2 = 234
        temp3 = 345
        temp4 = 456
        tempI1 = 987
        tempI2 = 876
        tempI3 = 765
        tempI4 = 654
        tps = 123
        ect = 333
        iat = 2313
        iap = 2092

        if clutch:
            self.canvas.itemconfig(self.clutchOn, state="normal")
        else:
            self.canvas.itemconfig(self.clutchOn, state="hidden")

        if brake:
            self.canvas.itemconfig(self.brakeOn, state="normal")
        else:
            self.canvas.itemconfig(self.brakeOn, state="hidden")

        if arrowLOn:
            self.canvas.itemconfig(self.arrowLOn, state="normal")
        else:
            self.canvas.itemconfig(self.arrowLOn, state="hidden")

        if arrowROn:
            self.canvas.itemconfig(self.arrowROn, state="normal")
        else:
            self.canvas.itemconfig(self.arrowROn, state="hidden")
        
        if gpsOn:
            self.heading.config(text=direction)
            self.b5.config(text=turn)

        self.canvas.delete("needle")

        self.speedNeedle2 = ImageTk.PhotoImage(self.speedNeedle.rotate(needleA))
        self.canvas.create_image(self.canvasW/2,self.canvasH/2, tag=("needle"), image = self.speedNeedle2)
        
        self.rpmNeedle2 = ImageTk.PhotoImage(self.rpmNeedle.rotate(needleB))
        self.canvas.create_image(self.canvasW/2,self.canvasH/2, tag=("needle"), image = self.rpmNeedle2)

        for each in self.gearList:
            self.canvasG.itemconfigure(each, state="hidden")
        self.canvasG.itemconfigure(gear, state="normal")

        self.speedNumber.config(text=abs(speed))
        self.temp1.config(text=temp1)
        self.temp2.config(text=temp2)
        self.temp3.config(text=temp3)
        self.temp4.config(text=temp4)

        self.temp1I.config(text=tempI1)   
        self.temp2I.config(text=tempI2)
        self.temp3I.config(text=tempI3)
        self.temp4I.config(text=tempI4)

        self.m1.config(text=tps)   
        self.m2.config(text=ect)
        self.m3.config(text=iat)
        self.m4.config(text=iap)

        gui.after(500, self.update)
        


    def rTest(self):
        ## If GPS is onj
        if gpsOn == True:
            gpsDir = ['North', 'East', 'South', 'West']
            self.heading.config(text=random.choice(gpsDir))
            nTurn = ['Straight', 'Left', 'Right', 'U-Turn']
            self.b5.config(text=random.choice(nTurn))

        gChoice = random.choice(self.gearList)
        
        for each in self.gearList:
            self.canvasG.itemconfigure(each, state="hidden")
        self.canvasG.itemconfigure(gChoice, state="normal")


        '''
        self.speed = self.speed + 1     
        self.rpm = self.rpm + 50
        
        if self.rpm >= 18000:
            self.rpm = 0

        if self.speed == 120:
            self.speed = 1
        '''

        self.speed = randint(1,120)
        self.rpm = randint(1,19000)

        needleA = 135 - (self.speed * 2.25)     # 360 - 90 = 270   270/120 = 2.25
        needleB = 135 - (self.rpm * 0.015)    #360 - 90 = 270    270/18000 = 0.015

        self.canvas.delete("needle")

        self.speedNeedle2 = ImageTk.PhotoImage(self.speedNeedle.rotate(needleA))
        self.canvas.create_image(self.canvasW/2,self.canvasH/2, tag=("needle"), image = self.speedNeedle2)
        
        self.rpmNeedle2 = ImageTk.PhotoImage(self.rpmNeedle.rotate(needleB))
        self.canvas.create_image(self.canvasW/2,self.canvasH/2, tag=("needle"), image = self.rpmNeedle2)

        if self.speed < 80:
            self.canvas.itemconfig(self.clutchOn, state="normal")
        else:
            self.canvas.itemconfig(self.clutchOn, state="hidden")
        
        if self.speed < 40:
            self.canvas.itemconfig(self.brakeOn, state="normal")
        else:
            self.canvas.itemconfig(self.brakeOn, state="hidden")
        
        if self.rpm > redLine:
            self.canvas.itemconfig(self.cImgRed, state="normal")
        else:
            self.canvas.itemconfig(self.cImgRed, state="hidden")
            
        self.speedNumber.config(text=abs(self.speed))
        self.temp1.config(text=randint(20,150))
        self.temp2.config(text=randint(20,150))
        self.temp3.config(text=randint(20,150))
        self.temp4.config(text=randint(20,150))

        self.temp1I.config(text=randint(20,150))
        self.temp2I.config(text=randint(20,150))
        self.temp3I.config(text=randint(20,150))
        self.temp4I.config(text=randint(20,150))
        gui.after(50, self.rTest)


    def setFrameBoxes(self):
        self.aRow[0] = StringVar()
        self.aRow[0] = Frame(self.tFrame)
        self.aRow[0].grid(row=0, column=0, columnspan=5, pady=20)
        self.lTime = Label(self.aRow[0], font=("", 30))
        self.lTime.grid(row=0, column=0)

        #self.wSet = Frame(self.tFrame, width=1000)
        #self.wSet.grid(row=1, column=0, columnspan=5)

        for i in range(0,5):
            self.bRow[i] = StringVar()
            self.bRow[i] = Frame(self.tFrame)
            self.bRow[i].grid(row=1, column=i, pady=40)
            self.eRow[i] = StringVar()
            self.eRow[i] = Frame(self.tFrame)
            self.eRow[i].grid(row=4, column=i)
            
        self.cRow[0] = StringVar()
        self.cRow[0] = Frame(self.tFrame, width=12)
        self.cRow[0].grid(row=2, column=0)
        
        self.cRow[1] = StringVar()
        self.cRow[1] = Frame(self.tFrame, width=12)
        self.cRow[1].grid(row=2, column=1)

        self.cRow[2] = StringVar()
        self.cRow[2] = Frame(self.tFrame, width=12)
        self.cRow[2].grid(row=2, column=2)

        self.cRow[3] = StringVar()
        self.cRow[3] = Frame(self.tFrame, width=12)
        self.cRow[3].grid(row=2, column=3, columnspan=2, rowspan=5, sticky="nesw")

        ###  Navigation

        if gpsOn == True:

            self.b2 = Label(self.bRow[0], text="Current Road", font=("", 30))
            self.b2.grid(row=0, column=0)

            self.heading = Label(self.bRow[1], text="Direction", font=("", 30), padx=20, width=7)
            self.heading.grid(row=0, column=0)

            self.b4 = Label(self.bRow[2], text="Distance", font=("", 30))
            self.b4.grid(row=0, column=0)

            self.b5 = Label(self.bRow[3], text="Next", font=("", 30), width=7, anchor=N)
            self.b5.grid(row=0, column=0)

            self.b6 = Label(self.bRow[4], text="Next road", font=("", 30), bg="red")
            self.b6.grid(row=0, column=0)

        ######  Temps
        self.temp1 = Label(self.cRow[0], text='Engine Temp 1: ', anchor=W)
        self.temp1.grid(row=0, column=0, sticky="nesw")
        self.temp2 = Label(self.cRow[0], text='Engine Temp 2: ', anchor=W)
        self.temp2.grid(row=1, column=0, sticky="nesw")
        self.temp3 = Label(self.cRow[0], text='Engine Temp 3: ', anchor=W)
        self.temp3.grid(row=2, column=0, sticky="nesw")
        self.temp4 = Label(self.cRow[0], text='Engine Temp 4: ', anchor=W)
        self.temp4.grid(row=3, column=0, sticky="nesw")

        self.temp1 = Label(self.cRow[0], anchor=N, width=3)
        self.temp1.grid(row=0, column=1, sticky="nesw")
        self.temp2 = Label(self.cRow[0], anchor=N, width=3)
        self.temp2.grid(row=1, column=1, sticky="nesw")
        self.temp3 = Label(self.cRow[0], anchor=N, width=3)
        self.temp3.grid(row=2, column=1, sticky="nesw")
        self.temp4 = Label(self.cRow[0], anchor=N, width=3)
        self.temp4.grid(row=3, column=1, sticky="nesw")

        self.temp1It = Label(self.cRow[1], text='Intake Temp 1: ', anchor=W)
        self.temp1It.grid(row=0, column=0, sticky="nesw")
        self.temp2It = Label(self.cRow[1], text='Intake Temp 2: ', anchor=W)
        self.temp2It.grid(row=1, column=0, sticky="nesw")
        self.temp3It = Label(self.cRow[1], text='Intake Temp 3: ', anchor=W)
        self.temp3It.grid(row=2, column=0, sticky="nesw")
        self.temp4It = Label(self.cRow[1], text='Intake Temp 4: ', anchor=W)
        self.temp4It.grid(row=3, column=0, sticky="nesw")

        self.temp1I = Label(self.cRow[1], anchor=N, width=3)
        self.temp1I.grid(row=0, column=1, sticky="nesw")
        self.temp2I = Label(self.cRow[1], anchor=N, width=3)
        self.temp2I.grid(row=1, column=1, sticky="nesw")
        self.temp3I = Label(self.cRow[1], anchor=N, width=3)
        self.temp3I.grid(row=2, column=1, sticky="nesw")
        self.temp4I = Label(self.cRow[1], anchor=N, width=3)
        self.temp4I.grid(row=3, column=1, sticky="nesw")

        self.m1 = Label(self.cRow[2], text='TPS: ', anchor=W)
        self.m1.grid(row=0, column=0, sticky="nesw")
        self.m2 = Label(self.cRow[2], text='ECT: ', anchor=W)
        self.m2.grid(row=1, column=0, sticky="nesw")
        self.m3 = Label(self.cRow[2], text='IAT: ', anchor=W)
        self.m3.grid(row=2, column=0, sticky="nesw")
        self.m4 = Label(self.cRow[2], text='IAP: ', anchor=W)
        self.m4.grid(row=3, column=0, sticky="nesw")

        self.m1 = Label(self.cRow[2], anchor=N, width=3)
        self.m1.grid(row=0, column=1, sticky="nesw")
        self.m2 = Label(self.cRow[2], anchor=N, width=3)
        self.m2.grid(row=1, column=1, sticky="nesw")
        self.m3 = Label(self.cRow[2], anchor=N, width=3)
        self.m3.grid(row=2, column=1, sticky="nesw")
        self.m4 = Label(self.cRow[2], anchor=N, width=3)
        self.m4.grid(row=3, column=1, sticky="nesw")

        thisFont=("System", 18)

        for i in self.cRow:
            self.cRow[i].grid(padx=10)
            for each in self.cRow[i].winfo_children():
                each.config(font=thisFont)
                each.grid(ipadx=2, ipady=2)

        ##### Gear

        self.canvasG = Canvas(self.eRow[0], bg="black", width=200, highlightthickness=0)
        self.canvasG.grid(row=0, column=0, sticky="n")

        self.speedNumber = Label(self.eRow[2], text="speed", font=("System", 80))
        self.speedNumber.grid(row=0, column=0, sticky='nesw')

        Label(self.eRow[1], text="I dont know\nright now").grid(row=1, column=0, sticky=N)  #Blank
        Label(self.eRow[2], text="MPH").grid(row=1, column=0, sticky=N)
    
        ### Speed Image

        ## MATH!!!!!!!
        ## 0mph = 135    160 mph= -225
        ## 360 / 160 = 2.25 per MPH

        self.speedB = Image.open('index/speedBackT.png')
        self.speedBRed = Image.open('index/speedBackRL.png')
        self.speedNeedle = Image.open('index/needleT.png')
        self.rpmNeedle = Image.open('index/needleRPMT.png')

        #self.speedB = self.speedB.resize((self.speedB.width * 2, self.speedB.height * 2))
        
        self.speedB = self.speedB.resize((int(screenW / 2), int(screenW / 2)))
        self.speedBRed = self.speedBRed.resize((int(screenW / 2), int(screenW / 2)))
        self.speedNeedle = self.speedNeedle.resize((int(screenW / 2), int(screenW / 2)))
        self.rpmNeedle = self.rpmNeedle.resize((int(screenW / 2), int(screenW / 2)))

        self.speedB2 = ImageTk.PhotoImage(self.speedB)
        self.speedB2Red = ImageTk.PhotoImage(self.speedBRed)

        self.canvasW = self.speedB2.width()
        self.canvasH = self.speedB2.height()

        self.canvas = Canvas(self.cRow[3], width=self.canvasW, height=self.canvasH, highlightthickness=0, bg="black")
        self.canvas.grid(row=0, column=0)
        self.cImg = self.canvas.create_image(self.canvasW/2, self.canvasH/2, image = self.speedB2)
        self.cImgRed = self.canvas.create_image(self.canvasW/2, self.canvasH/2, state = "hidden", image = self.speedB2Red)



        ##### Clutch / Brake
        self.clutch = Image.open('index/clutchT.png')
        self.brake = Image.open('index/brakeT.png')

        self.clutch = self.clutch.resize((int(screenW / 2), int(screenW / 2)))
        self.brake = self.brake.resize((int(screenW / 2), int(screenW / 2)))
        self.clutch = ImageTk.PhotoImage(self.clutch)
        self.brake = ImageTk.PhotoImage(self.brake)

        self.clutchOn = self.canvas.create_image(self.canvasW/2,self.canvasH/2, state="hidden", image = self.clutch)
        self.brakeOn = self.canvas.create_image(self.canvasW/2,self.canvasH/2, state="hidden", image = self.brake)

        #####  Signals
        self.arrowL = Image.open('index/arrowLT.png')
        self.arrowR = Image.open('index/arrowRT.png')

        self.arrowL = self.arrowL.resize((int(screenW / 2), int(screenW / 2)))
        self.arrowR = self.arrowR.resize((int(screenW / 2), int(screenW / 2)))
        self.arrowL = ImageTk.PhotoImage(self.arrowL)
        self.arrowR = ImageTk.PhotoImage(self.arrowR)

        self.arrowLOn = self.canvas.create_image(self.canvasW/2,self.canvasH/2, state="hidden", image = self.arrowL)
        self.arrowROn = self.canvas.create_image(self.canvasW/2,self.canvasH/2, state="hidden", image = self.arrowR)
        
        frameList = [self.aRow, self.eRow]

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
