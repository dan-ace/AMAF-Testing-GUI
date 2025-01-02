import tkinter
import customtkinter as ctk # <- import the CustomTkinter module
from tkinter import filedialog

from statistics import mean
import numpy as np
import glob
import os
import os.path
import subprocess
import json
from datetime import datetime
from functools import reduce
import time

ctk.set_appearance_mode("dark")


class labels():
    def __init__(self, parent, name, varText):

        self.parent=parent
        self.name=name
        self.varText=varText
        self.label = ctk.CTkLabel(parent,text=varText)
    
    def place(self, **kwargs):
        self.label.place(**kwargs)


class myButton():
    def __init__(self, parent, color, hoverColor, width, height, varText, font,  functCommand=None):
        self.parent=parent
        self.varText=varText
        self.width=width
        self.height=height
        self.color=color
        self.hoverColor=hoverColor
        self.functCommand=functCommand
        self.font=font
        self.button = ctk.CTkButton(parent,text=varText,font=self.font,fg_color=self.color,hover_color=self.hoverColor,command=functCommand,width=self.width,height=self.height)

    def place(self, **kwargs):
        self.button.place(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def configure(self, **kwargs):
        self.button.configure(**kwargs)

    def state(self, **kwargs):
        self.button.state(**kwargs)

    def getState(self):
        return self.button.cget('state')

class Interlock_InnerFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=400, height=600, fg_color='#e9edf6', **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.interlockLabel = ctk.CTkLabel(self, text="        Interlocks", font=ctk.CTkFont("Roboto",25), text_color="black")
        self.interlockLabel.grid(row=0,column=0,sticky='ew',padx=5,pady=5)

        self.DCS_Interlock = ctk.CTkSwitch(self)
        self.DCS_Interlock.grid(row=1,column=0,sticky='ew',padx=5,pady=5)

        #self.testButton = ctk.CTkButton(self, text="test",command = parent.parent.openTerminalTest, font=self.customFont)
        #self.testButton.grid(row=2,column=0,sticky='ew',padx=25,pady=15)

    
    
class Interlock_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=400, height=600, fg_color='grey', **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.testButton = ctk.CTkButton(self, text="test",command = parent.runRaspiInterlock, font=self.customFont)
        self.testButton.grid(row=2,column=0,sticky='ew',padx=25,pady=15)

        self.DCStestButton = ctk.CTkButton(self, text="test",command = parent.runDCSInterlock, font=self.customFont)
        self.DCStestButton.grid(row=3,column=0,sticky='ew',padx=25,pady=15)

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)

        #self.innerFrame = Interlock_InnerFrame(parent=self)
        #self.innerFrame.grid(row=0,column=0,sticky='nesw',padx=5,pady=5)
    
class YARR_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=270, height=600, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)
        
        self.itkpixN_label = ctk.CTkLabel(self, text="Select ANL_ITkPix number:",font=self.customFont)
        self.itkpixN_label.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

        self.itkpixN_box = ctk.CTkOptionMenu(self,values=[str(i) for i in range(1,33)],font=self.customFont)
        self.itkpixN_box.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)

        self.testType_label = ctk.CTkLabel(self, text="Select test type: ",font=self.customFont)
        self.testType_label.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

        self.testType_box = ctk.CTkOptionMenu(self,values=["Basic","EYE","MHT","TUN","PFA"],font=self.customFont)
        self.testType_box.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

        self.localdb_ask = ctk.CTkLabel(self,text="Upload to Local DB?",font=self.customFont)
        self.localdb_ask.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)

        self.radioval=ctk.IntVar()

        self.localdb_yes = ctk.CTkRadioButton(self, variable=self.radioval, text="Yes", value=1,font=self.customFont)
        self.localdb_yes.place(relx=0.4,rely=0.56,anchor=tkinter.CENTER)
        
        self.localdb_no = ctk.CTkRadioButton(self, variable=self.radioval, text="No", value=0,font=self.customFont)
        self.localdb_no.place(relx=0.6,rely=0.56,anchor=tkinter.W)
        

        self.runTestButton = ctk.CTkButton(self, text="Run Test",fg_color="green",hover_color="darkgreen",command=parent.runYarrTest,font=self.customFont)
        self.runTestButton.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)

class MQT_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=250, height=600, **kwargs)
        self.customFont = ctk.CTkFont("Roboto",20)

        self.itkpixN_label = ctk.CTkLabel(self, text="Select ANL_ITkPix number:",font=self.customFont)
        self.itkpixN_label.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

        self.itkpixN_box = ctk.CTkOptionMenu(self,values=[str(i) for i in range(1,33)],font=self.customFont)
        self.itkpixN_box.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)

        self.testType_label = ctk.CTkLabel(self, text="Select test type: ",font=self.customFont)
        self.testType_label.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

        self.testType_box = ctk.CTkOptionMenu(self,values=["IV-MEASURE","ADC-CALIBRATION","ANALOG-READBACK","SLDO","VCAL-CALIBRATION","DATA-TRANSMISSION","INJECTION-CAPACITANCE","LP-MODE","OVERVOLTAGE-PROTECTION","UNDERSHUNT-PROTECTION"],font=self.customFont)
        self.testType_box.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

        self.localdb_ask = ctk.CTkLabel(self,text="Upload to Local DB?",font=self.customFont)
        self.localdb_ask.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)

        self.radioval=ctk.IntVar()

        self.localdb_yes = ctk.CTkRadioButton(self, variable=self.radioval, text="Yes", value=1,font=self.customFont)
        self.localdb_yes.place(relx=0.4,rely=0.56,anchor=tkinter.CENTER)

        self.localdb_no = ctk.CTkRadioButton(self, variable=self.radioval, text="No", value=0,font=self.customFont)
        self.localdb_no.place(relx=0.6,rely=0.56,anchor=tkinter.W)


        self.runTestButton = ctk.CTkButton(self, text="Run Test",fg_color="green",hover_color="darkgreen",command=parent.runMQTtest,font=self.customFont)
        self.runTestButton.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)


        
class DCS_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, width=450, height=600, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)
        
        #chiller options
        self.chillerOn = myButton(self,'green','darkgreen',160,40,'Turn Chiller On',self.customFont,parent.turnChillerOn)
        self.chillerOn.grid(row=0,column=0,sticky='ew',padx=30,pady=10)

        self.chillerValueLabel = ctk.CTkLabel(self, text="Set Chiller Temp (C): ", font=self.customFont)
        self.chillerValueLabel.grid(row=0,column=4,sticky="e",padx=30,pady=5)
        
        self.chillerValue = ctk.CTkEntry(self, width=50, height=30, font=self.customFont)
        self.chillerValue.grid(row=0,column=5,sticky="w",pady=5)
        self.chillerValue.insert(0,"15")

        self.chillerOff = myButton(self,'red','darkred',160,40,'Turn Chiller Off',self.customFont,parent.turnChillerOff)
        self.chillerOff.grid(row=1,column=0,sticky='ew',padx=30,pady=10)

        
        self.rowconfigure(2,minsize=40)

        #HV options
        self.HV_On = myButton(self,'green','darkgreen',160,40,'Turn HV On',self.customFont,parent.turnHV_On)
        self.HV_On.grid(row=3,column=0,sticky='ew',padx=30,pady=10)

        self.HV_valueLabel = ctk.CTkLabel(self, text="Set HV Value (V): ", font=self.customFont)
        self.HV_valueLabel.grid(row=3,column=4,sticky="e",padx=30,pady=5)

        self.HV_value = ctk.CTkEntry(self, width=50, height=30, font=self.customFont)
        self.HV_value.grid(row=3,column=5,sticky="w",pady=5)
        self.HV_value.insert(0,"0")
        
        self.HV_Off = myButton(self,'red','darkred',160,40,'Turn HV Off',self.customFont,parent.turnHV_Off)
        self.HV_Off.grid(row=4,column=0,sticky='ew',padx=30,pady=10)

        
        self.rowconfigure(5,minsize=40)

        #LV options
        self.LV_On = myButton(self,'green','darkgreen',160,40,'Turn LV On',self.customFont,parent.turnLV_On)
        self.LV_On.grid(row=6,column=0,sticky='ew',padx=30,pady=10)

        self.LV_valueLabel = ctk.CTkLabel(self, text="Set LV: ", font=self.customFont)
        self.LV_valueLabel.grid(row=6,column=4,sticky="e",padx=30,pady=5)

        """
        self.LV_V = ctk.CTkEntry(self, width=50, height=30, font=self.customFont)
        self.LV_V.grid(row=6,column=5,sticky="w",pady=5)
        self.LV_V.insert(0,"0")

        self.V_label = ctk.CTkLabel(self, text="V , ",font=self.customFont)
        self.V_label.grid(row=6,column=6, sticky='w',padx=10,pady=5)

        self.LV_I = ctk.CTkEntry(self, width=50, height=30, font=self.customFont)
        self.LV_I.grid(row=6,column=7, sticky="w",pady=5)
        self.LV_I.insert(0,"0")

        self.I_label = ctk.CTkLabel(self, text="I",font=self.customFont)
        self.I_label.grid(row=6,column=8, sticky="w",padx=10,pady=5)
        """

        self.LV_Value =  ctk.CTkOptionMenu(self,values=["2.1 V, 5.88 A","2.1 V, 6.60 A","2.1 V, 4.41 A"],font=self.customFont)
        self.LV_Value.grid(row=6,column=5,columnspan=3,sticky='w',pady=5)


        self.LV_Off = myButton(self,'red','darkred',160,40,'Turn LV Off',self.customFont,parent.turnLV_Off)
        self.LV_Off.grid(row=7,column=0,sticky='ew',padx=30,pady=10)

        
        self.rowconfigure(8,minsize=40)

        
        self.PeltierOn = myButton(self,'green','darkgreen',160,40,'Turn Peltier On',self.customFont,parent.turnPeltierOn)
        self.PeltierOn.grid(row=9,column=0,sticky='ew',padx=30,pady=10)

        self.PeltierSetLabel = ctk.CTkLabel(self, text="Set Peltier: ",font=self.customFont)
        self.PeltierSetLabel.grid(row=9,column=4,sticky='e',padx=30,pady=5)

        self.PeltierV = ctk.CTkEntry(self, width=50, height=30, font=self.customFont)
        self.PeltierV.grid(row=9,column=5,sticky="w",pady=5)
        self.PeltierV.insert(0,"2")

        self.PeltierVLabel = ctk.CTkLabel(self, text=" V,  ", font=self.customFont)
        self.PeltierVLabel.grid(row=9,column=6,sticky='W',padx=5,pady=5)

        self.PeltierPolarity =  ctk.CTkOptionMenu(self,values=["cool","heat"],font=self.customFont, width=100)
        self.PeltierPolarity.grid(row=9,column=7,sticky='w',pady=5)


        self.PeltierOff = myButton(self,'red','darkred',160,40,'Turn Peltier Off',self.customFont,parent.turnPeltierOff)
        self.PeltierOff.grid(row=10,column=0,sticky='ew',padx=30,pady=10)

        self.rowconfigure(11,minsize=40)

        self.ReadySource = myButton(self,'green','darkgreen',160,40,'Ready Source',self.customFont,parent.readySource)
        self.ReadySource.grid(row=12,column=0,sticky='ew',padx=30,pady=10)

        self.ParkSource = myButton(self,'red','darkred',160,40,'Park Source',self.customFont,parent.parkSource)
        self.ParkSource.grid(row=13,column=0,sticky='ew',padx=30,pady=10)

        self.SourceLabel = ctk.CTkLabel(self,text='Move Source To: ', font=self.customFont)
        self.SourceLabel.grid(row=12,column=4,sticky='e',padx=30,pady=5)

        self.SourceValue = ctk.CTkOptionMenu(self, values=["Chip 1","Chip 2","Chip 3","Chip 4", "Center"], font=self.customFont)
        self.SourceValue.grid(row=12,column=5,columnspan=3,sticky='w',pady=5)

        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1750x900")
        self.minsize(1750,900)
        self.title("Electrical Testing!")
        self.resizable(True,True)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3),weight=1)

        self.Interlock_options = Interlock_Frame(parent=self)
        self.Interlock_options.grid(row=0,column=0, rowspan=2, sticky='nesw')

        self.YARR_label = ctk.CTkLabel(self, text = "YARR",font=("Roboto",25))
        self.YARR_label.grid(row=0,column=1,sticky='ew',padx=25,pady=10)

        self.YARR_options = YARR_Frame(parent=self)
        #self.YARR_options.place(relx=0.3,rely=0.55, anchor=tkinter.CENTER)
        self.YARR_options.grid(row=1,column=1,sticky='nesw',padx=25,pady=15)

        self.MQT_label = ctk.CTkLabel(self, text = "MQT", font=("Roboto",25))
        self.MQT_label.grid(row=0,column=2,sticky='ew',padx=25,pady=15)

        self.MQT_options = MQT_Frame(parent=self)
        self.MQT_options.grid(row=1,column=2,sticky='nesw',padx=25,pady=15)
        
        self.DCS_label = ctk.CTkLabel(self, text = "DCS", font=("Roboto",25))
        self.DCS_label.grid(row=0,column=3,sticky='ew',padx=25,pady=10)

        self.DCS_options = DCS_Frame(parent=self)
        #self.DCS_options.place(relx=0.7,rely=0.55, anchor=tkinter.CENTER)
        self.DCS_options.grid(row=1,column=3,sticky='nesw',padx=25,pady=15)

        self.customFont = ctk.CTkFont("Roboto",20)

        #testbuttonforopening a new terminal
        self.testButton = ctk.CTkButton(self, text="test",command = self.openTerminalTest)
        self.testButton.grid(row=0,column=4,sticky='nesw',padx=25,pady=15)

        #self.sshtestButton = ctk.CTkButton(self, text="test",command = self.opensshTerminalTest)
        #self.sshtestButton.grid(row=1,column=4,sticky='nesw',padx=25,pady=15)


    def openTerminalTest(self):

        
        #os.system('gnome-terminal -- /home/itktestsetup2/ITk/forGUI/venv/bin/python3.11 mockinterlock.py')

        #p = subprocess.Popen(['/home/itktestsetup2/ITk/forGUI/venv/bin/python3.11', ' /home/itktestsetup2/ITk/forGUI/mockinterlock.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)

        #output, errors = p.communicate()
        #print(output)
        #to_run = "python3.11 mockinterlock.py"
        #subprocess.Popen(['xfce4-terminal',  '-e', to_run])

        #os.system("start cmd /K python3.11 mockinterlock.py")

        #process = subprocess.Popen("sudo gnome-terminal -- python3.11 mockinterlock.py",
                                   #stdout=subprocess.PIPE,
                                   #stderr=None,
                                   #shell=True
                                #)
        #output, error = process.communicate()

        #print(output)

        code=subprocess.call(['gnome-terminal', "--", "python3.11", "mockinterlock.py"])
        print("mock interlock code: ",str(code))
        #newterminal.wait()
        #command = 'ls -l'
        #subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command, '--window'])

        #subprocess.call(["ssh","raspif@192.168.0.202","python3.9 /home/raspif/imagin/runAllInterlocks.py"],stdout=subprocess.PIPE)


    def runRaspiInterlock(self):
        try:
            code=subprocess.call(['gnome-terminal', "--","ssh","raspif@192.168.0.202", "python3.9 /home/raspif/imagin/runAllInterlocks.py"])
            print("raspi interlock code: ",str(code))
        except:
            code=subprocess.call(['gnome-terminal', "--", "python3.11", "mockinterlock.py"])
            print("mock interlock code: ",str(code))
            
    def runDCSInterlock(self):
        try:
            code=subprocess.call(['gnome-terminal', "--", "python3.6","/home/itktestsetup2/ITk/anl_itk/DCSMonitoring/ControlInterlock.py"])
            print("dcs interlock code: ",str(code))
        except:
            code=subprocess.call(['gnome-terminal', "--", "python3.11", "mockinterlock.py"])
            print("mock interlock code: ",str(code))
        
    def runYarrTest(self):
        localdb = self.YARR_options.radioval.get()
        testType = self.YARR_options.testType_box.get()
        itkpixnum = self.YARR_options.itkpixN_box.get()
        script_path = '/home/itkpixsetup2/ITk/Yarr/YARR_TestRunner.py'
        script_dir = os.path.dirname(script_path)
        commands = ["/home/itkpixsetup2/ITk/module-qc-database-tools/venv/bin/python3.11", script_path, "-t", "ITkPix", "-i", itkpixnum]
        if testType=="Basic":
            subprocess.Popen(commands, cwd=script_dir)
            print(commands)
        else:
            commands.append("-r")
            commands.append(testType)
            if localdb==1:
                commands.append("-l")
            print(commands)
            subprocess.Popen(commands, cwd=script_dir)

    def runMQTtest(self):
        localdb = self.MQT_options.radioval.get()
        testType = self.MQT_options.testType_box.get()
        itkpixnum = self.MQT_options.itkpixN_box.get()
        script_path = '/home/itkpixsetup2/ITk/module-qc-tools/MQT_TestRunner.py'
        script_dir = os.path.dirname(script_path)
        commands = ["/home/itkpixsetup2/ITk/module-qc-database-tools/venv/bin/python3.11", script_path, "-t", "ITkPix", "-i", itkpixnum]
        if testType=="Basic":
            subprocess.Popen(commands, cwd=script_dir)
            print(commands)
        else:
            commands.append("-r")
            commands.append(testType)
            if localdb==1:
                commands.append("-l")
                print(commands)
                subprocess.Popen(commands, cwd=script_dir)

        
        
    def turnChillerOn(self):
        onButState = self.DCS_options.chillerOn.getState()
        offButState = self.DCS_options.chillerOff.getState()
        if offButState=="disabled":
            self.DCS_options.chillerOff.configure(state="normal")
            self.DCS_options.chillerOn.configure(state="disabled")
        else:
            self.DCS_options.chillerOn.configure(state="disabled")
        print("Chiller Turning On")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/chillerTest.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "on",str(self.DCS_options.chillerValue.get())]
        subprocess.Popen(commands, cwd=script_dir)
        
    def turnChillerOff(self):
        onButState = self.DCS_options.chillerOn.getState()
        offButState = self.DCS_options.chillerOff.getState()
        if onButState=="disabled":
            self.DCS_options.chillerOn.configure(state="normal")
            self.DCS_options.chillerOff.configure(state="disabled")
        else:
            self.DCS_options.chillerOff.configure(state="disabled")
        print("Chiller Turning Off")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/chillerTest.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "off","15"]
        subprocess.Popen(commands, cwd=script_dir)

    def turnHV_On(self):
        print("HV Turning On")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/HVControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--poweron","--setcurrent",f'" {self.DCS_options.HV_value},0.00002"']
        subprocess.Popen(commands, cwd=script_dir)
    
    def turnHV_Off(self):
        print("HV Turning Off")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/HVControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--poweroff"]
        subprocess.Popen(commands, cwd=script_dir)

    def turnLV_On(self):
        print("LV Turning On")
        V_A_Entry = self.DCS_options.LV_Value.get()
        V_A = "0.00"
        if V_A_Entry=="2.1 V, 5.88 A":
            V_A = '2.1,5.88'
        elif V_A_Entry=="2.1 V, 6.60 A":
            V_A = '2.1,6.60'
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/LVControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--poweron","--setcurrent",V_A]
        subprocess.Popen(commands, cwd=script_dir)

    
    def turnLV_Off(self):
        print("LV Turning Off")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/LVControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--poweroff"]
        subprocess.Popen(commands, cwd=script_dir)

    def turnPeltierOn(self):
        print("Peltier Turning On")
        heatOrCool = self.DCS_options.PeltierPolarity.get()
        if int(self.DCS_options.PeltierV.get())>8:
            print("Desired Peltier Voltage is above 8 V. Choose a Voltage at or below 8 V.")
            return
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/PeltierControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "-s","on","-v",str(self.DCS_options.PeltierV.get()),"-p",heatOrCool]
        subprocess.Popen(commands, cwd=script_dir)

    def turnPeltierOff(self):
        print("Peltier Turning Off")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/PeltierControl.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "-s","off"]
        subprocess.Popen(commands, cwd=script_dir)

    def readySource(self):
        sourceLoc = self.DCS_options.SourceValue.get()
        sourceLocInt = 0
        if sourceLoc=="Chip 1":
            sourceLocInt = 1
        elif sourceLoc=="Chip 2":
            sourceLocInt = 2
        elif sourceLoc=="Chip 3":
            sourceLocInt = 3
        elif sourceLoc=="Chip 4":
            sourceLocInt = 4
        elif sourceLoc=="Center":
            sourceLocInt = 0
            
        print("Moving Source To Module")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/ControlMotor.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--position",str(sourceLocInt)]
        subprocess.Popen(commands, cwd=script_dir)

    def parkSource(self):
        print("Parking Source")
        script_path = '/home/itkpixsetup2/ITk/anl_itk/DCSMonitoring/ControlMotor.py'
        script_dir = os.path.dirname(script_path)
        commands = ["python3.6", script_path, "--park"]
        subprocess.Popen(commands, cwd=script_dir)


app = App()
app.mainloop()
