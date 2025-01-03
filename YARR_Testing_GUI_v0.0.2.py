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

ctk.set_appearance_mode("light")
        
    

class myTitleButton1():
    def __init__(self,
                 parent,
                 color,
                 hoverColor,
                 textColor,
                 width,
                 height,
                 varText,
                 font,
                 functCommand=None,
                 other_buttons=None,
                 is_clicked=False):
        self.parent=parent
        self.varText=varText
        self.width=width
        self.height=height
        self.color=color
        self.hoverColor=hoverColor
        self.functCommand=functCommand
        self.font=font
        self.textColor=textColor
        self.is_clicked=is_clicked
        self.other_buttons=other_buttons
        self.button = ctk.CTkButton(parent,
                                    text=varText,
                                    font=self.font,
                                    text_color=self.textColor,
                                    fg_color=self.color,
                                    corner_radius=2,
                                    command=self.onClick,
                                    hover_color=self.hoverColor,width=self.width,height=self.height)

    def place(self, **kwargs):
        self.button.place(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def bind(self, sequence, func, add=None):
        self.button.bind(sequence, func)

    def configure(self, **kwargs):
        self.button.configure(**kwargs)

    def state(self, **kwargs):
        self.button.state(**kwargs)

    def getState(self):
        return self.button.cget('state')

    def onClick(self):
        if not self.is_clicked:
            self.is_clicked=True
            for other_button in self.other_buttons:
                other_button.is_clicked = False
                other_button.button.configure(text_color='#d6d1cd')
            if self.functCommand:
                self.functCommand()

class myTitleButton2():
    def __init__(self,
                 parent,
                 color,
                 hoverColor,
                 textColor,
                 width,
                 height,
                 varText,
                 font,
                 functCommand=None,
                 other_buttons=None,
                 is_clicked=False):
        self.parent=parent
        self.varText=varText
        self.width=width
        self.height=height
        self.color=color
        self.hoverColor=hoverColor
        self.functCommand=functCommand
        self.font=font
        self.textColor=textColor
        self.is_clicked=is_clicked
        self.other_buttons=other_buttons
        self.button = ctk.CTkButton(parent,
                                    text=varText,
                                    font=self.font,
                                    text_color=self.textColor,
                                    fg_color=self.color,
                                    corner_radius=2,
                                    command=self.onClick,
                                    hover_color=self.hoverColor,
                                    width=self.width,
                                    height=self.height)

    def place(self, **kwargs):
        self.button.place(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def bind(self, sequence, func, add=None):
        self.button.bind(sequence, func)

    def configure(self, **kwargs):
        self.button.configure(**kwargs)

    def state(self, **kwargs):
        self.button.state(**kwargs)

    def getState(self):
        return self.button.cget('state')

    def onClick(self):
        if not self.is_clicked:
            self.is_clicked=True
            for other_button in self.other_buttons:
                other_button.is_clicked = False
                other_button.button.configure(text_color='#666666')
            if self.functCommand:
                self.functCommand()

class myButton():
    def __init__(self,
                 parent,
                 color,
                 hoverColor,
                 textColor,
                 width,
                 height,
                 varText,
                 font,
                 functCommand=None,
                 cornerRad=10):
        self.parent=parent
        self.varText=varText
        self.width=width
        self.height=height
        self.color=color
        self.hoverColor=hoverColor
        self.functCommand=functCommand
        self.font=font
        self.textColor=textColor
        self.cornerRad=cornerRad
        self.button = ctk.CTkButton(parent,
                                    text=varText,
                                    font=self.font,
                                    text_color=self.textColor,
                                    fg_color=self.color,
                                    corner_radius=self.cornerRad,
                                    command=self.onClick,
                                    hover_color=self.hoverColor,
                                    width=self.width,
                                    height=self.height)

    def place(self, **kwargs):
        self.button.place(**kwargs)

    def grid(self, **kwargs):
        self.button.grid(**kwargs)

    def bind(self, sequence, func, add=None):
        self.button.bind(sequence, func)

    def configure(self, **kwargs):
        self.button.configure(**kwargs)

    def state(self, **kwargs):
        self.button.state(**kwargs)

    def getState(self):
        return self.button.cget('state')

    def onClick(self):
        if self.functCommand:
            self.functCommand()





class myLabel():
    def __init__(self, parent, color, width, height, varText, font):

        self.parent=parent
        self.varText=varText
        self.color=color
        self.width=width
        self.height=height
        self.font=font
        self.label = ctk.CTkLabel(parent,
                                  text=self.varText,
                                  text_color=self.color,
                                  width=self.width,
                                  height=self.height,
                                  font=self.font)


    def grid(self, **kwargs):
        self.label.grid(**kwargs)

    def bind(self, **kwargs):
        self.label.bind(**kwargs)

class mySwitch(ctk.CTkSwitch):
    def __init__(self, parent, **kwargs):
        super().__init__(parent,
                         font=ctk.CTkFont("Roboto",20),
                         progress_color='#61d095',
                         button_color='#F5e5ed',
                         button_hover_color='#d6d1cd',
                         fg_color='#ed6a5a',
                         **kwargs)

class myCheckBox(ctk.CTkCheckBox):
    def __init__(self, parent, **kwargs):
        super().__init__(parent,
                         onvalue="on",
                         offvalue="off",
                         fg_color="#61d095",
                         hover_color='#2f9d62',
                         text_color="#0d0b1e",
                         font=ctk.CTkFont("Roboto",15),
                         **kwargs)

class Selection_Bar(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent,
                         fg_color='#f5efed',
                         corner_radius=2,
                         **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.borderFrame = ctk.CTkFrame(self, height=5, fg_color='#0d0b1e', corner_radius=2)
        self.borderFrame.grid(row=8,column=0,columnspan=11,sticky='esw')

        self.YarrButton = myTitleButton1(self,'#f5efed','#f5efed','#0d0b1e',100,30,"YARR",self.customFont,parent.switchToYarr, is_clicked=True)
        self.MQTButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"MQT",self.customFont,parent.switchToMQT)
        self.MQATButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"MQAT",self.customFont,parent.switchToMQAT)
        self.MQDTButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"MQDT",self.customFont,parent.switchToMQDT)
        self.FullQCButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"Full QC",self.customFont,parent.switchToFullQC)

        self.YarrButton.other_buttons=[self.MQTButton,self.MQATButton,self.MQDTButton,self.FullQCButton]
        self.MQTButton.other_buttons=[self.YarrButton,self.MQATButton,self.MQDTButton,self.FullQCButton]
        self.MQATButton.other_buttons=[self.YarrButton,self.MQTButton,self.MQDTButton,self.FullQCButton]
        self.MQDTButton.other_buttons=[self.YarrButton,self.MQTButton,self.MQATButton,self.FullQCButton]
        self.FullQCButton.other_buttons=[self.YarrButton,self.MQTButton,self.MQATButton,self.MQDTButton]

        self.YarrButton.grid(row=7,column=0,sticky='nesw')
        self.MQTButton.grid(row=7,column=1,sticky='nesw')
        self.MQATButton.grid(row=7,column=2,sticky='nesw')
        self.MQDTButton.grid(row=7,column=3,sticky='nesw')
        self.FullQCButton.grid(row=7,column=4,sticky='nesw')

        self.YarrButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.YarrButton))
        self.YarrButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.YarrButton))

        self.MQTButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.MQTButton))
        self.MQTButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.MQTButton))

        self.MQATButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.MQATButton))
        self.MQATButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.MQATButton))

        self.MQDTButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.MQDTButton))
        self.MQDTButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.MQDTButton))

        self.FullQCButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.FullQCButton))
        self.FullQCButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.FullQCButton))


class Yarr_Test_Frame(ctk.CTkFrame):
    def	__init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", border_width=4, border_color="#858188", corner_radius=10, **kwargs)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        self.eyeDiaVar_MHT = ctk.StringVar(value="off")
        self.eyeDiaCheckBox_MHT = myCheckBox(self, text="Eye Diagram (MHT)", variable=self.eyeDiaVar_MHT, width=20, height=10)

        self.digScanVar_MHT = ctk.StringVar(value="off")
        self.digScanCheckBox_MHT = myCheckBox(self, text="Digital Scan (MHT)", variable=self.digScanVar_MHT, width=20, height=10)

        self.anaScanVar_MHT = ctk.StringVar(value="off")
        self.anaScanCheckBox_MHT = myCheckBox(self, text="Analog Scan (MHT)", variable=self.anaScanVar_MHT, width=20, height=10)

        self.threshScanHrVar_MHT = ctk.StringVar(value="off")
        self.threshScanHrCheckBox_MHT = myCheckBox(self, text="Threshold Scan HR (MHT)", variable=self.threshScanHrVar_MHT, width=20, height=10)

        self.totScanVar_MHT = ctk.StringVar(value="off")
        self.totScanCheckBox_MHT = myCheckBox(self, text="TOT Scan (MHT)", variable=self.totScanVar_MHT, width=20, height=10)

        self.eyeDiaCheckBox_MHT.grid(row=1, column=1, columnspan=2, sticky='w')
        self.digScanCheckBox_MHT.grid(row=3,column=1, columnspan=2, sticky='w')
        self.anaScanCheckBox_MHT.grid(row=5,column=1, columnspan=2, sticky='w')
        self.threshScanHrCheckBox_MHT.grid(row=7, column=1, columnspan=2, sticky='w')
        self.totScanCheckBox_MHT.grid(row=9, column=1, columnspan=2, sticky='w')

        self.clearChipConfigVar_TUN = ctk.StringVar(value="off")
        self.clearChipConfigCheckBox_TUN = myCheckBox(self, text="Clear Chip Config (TUN)", variable=self.clearChipConfigVar_TUN, width=20, height=10)

        self.threshScanHrVar_TUN = ctk.StringVar(value="off")
        self.threshScanHrCheckBox_TUN = myCheckBox(self, text="Threshold Scan HR (TUN)", variable=self.threshScanHrVar_TUN, width=20, height=10)

        self.totScanVar_TUN = ctk.StringVar(value="off")
        self.totScanCheckBox_TUN = myCheckBox(self, text="TOT Scan (TUN)", variable=self.totScanVar_TUN, width=20, height=10)

        self.tuneGlobalThreshVar_TUN = ctk.StringVar(value="off")
        self.tuneGlobalThreshCheckBox_TUN = myCheckBox(self, text="Tune Global Threshold (TUN)", variable=self.tuneGlobalThreshVar_TUN, width=20, height=10)

        self.tunePixelThreshVar_TUN = ctk.StringVar(value="off")
        self.tunePixelThreshCheckBox_TUN = myCheckBox(self, text="Tune Pixel Threshold (TUN)", variable=self.tunePixelThreshVar_TUN, width=20, height=10)

        self.threshScanHdVar_TUN = ctk.StringVar(value="off")
        self.threshScanHdCheckBox_TUN = myCheckBox(self, text="Threshold Scan HD (TUN)", variable=self.threshScanHdVar_TUN, width=20, height=10)

        self.totScan2Var_TUN = ctk.StringVar(value="off")
        self.totScan2CheckBox_TUN = myCheckBox(self, text="Second TOT Scan (end of TUN)", variable=self.totScan2Var_TUN, width=20, height=10)

        self.clearChipConfigCheckBox_TUN.grid(row=11, column=1, columnspan=2, sticky='w')
        self.threshScanHrCheckBox_TUN.grid(row=1, column=4, columnspan=2, sticky='w')
        self.totScanCheckBox_TUN.grid(row=3, column=4, columnspan=2, sticky='w')
        self.tuneGlobalThreshCheckBox_TUN.grid(row=5,column=4, columnspan=2, sticky='w')
        self.tunePixelThreshCheckBox_TUN.grid(row=7,column=4, columnspan=2, sticky='w')
        self.threshScanHdCheckBox_TUN.grid(row=9,column=4, columnspan=2, sticky='w')
        self.totScan2CheckBox_TUN.grid(row=11, column=4, columnspan=2, sticky='w')

        self.digScanVar_PFA = ctk.StringVar(value="off")
        self.digScanCheckBox_PFA = myCheckBox(self, text="Digital Scan (PFA)", variable=self.digScanVar_PFA, width=20, height=10)

        self.anaScanVar_PFA = ctk.StringVar(value="off")
        self.anaScanCheckBox_PFA = myCheckBox(self, text="Analog Scan (PFA)", variable=self.anaScanVar_PFA, width=20, height=10)

        self.threshScanHdVar_PFA = ctk.StringVar(value="off")
        self.threshScanHdCheckBox_PFA = myCheckBox(self, text="Threshold Scan HD (PFA)", variable=self.threshScanHdVar_PFA, width=20, height=10)

        self.noiseScanVar_PFA = ctk.StringVar(value="off")
        self.noiseScanCheckBox_PFA = myCheckBox(self, text="Noise Scan (PFA)", variable=self.noiseScanVar_PFA, width=20, height=10)
        
        self.discBumpScanVar_PFA = ctk.StringVar(value="off")
        self.discBumpScanCheckBox_PFA = myCheckBox(self, text="Disconnected Bump Scan (PFA)", variable=self.discBumpScanVar_PFA, width=20, height=10)

        self.mergedBumpScanVar_PFA = ctk.StringVar(value="off")
        self.mergedBumpScanCheckBox_PFA = myCheckBox(self, text="Merged Bump Scan (PFA)", variable=self.mergedBumpScanVar_PFA, width=20, height=10)

        self.retuneAndZeroBiasThreshScanVar_PFA = ctk.StringVar(value="off")
        self.retuneAndZeroBiasThreshScanCheckBox_PFA = myCheckBox(self, text="Retune Pixel Threshold/Zero Bias Threshold Scan\n/Reset Chip Configs (end of PFA)", variable=self.retuneAndZeroBiasThreshScanVar_PFA, width=20, height=10)

        self.sourceScanVar_PFA = ctk.StringVar(value="off")
        self.sourceScanCheckBox_PFA = myCheckBox(self, text="50 min. Source Scan", variable=self.sourceScanVar_PFA, width=20, height=20)

        self.digScanCheckBox_PFA.grid(row=13, column=4, columnspan=2, sticky='w')
        self.anaScanCheckBox_PFA.grid(row=1, column=7, columnspan=2, sticky='w')
        self.threshScanHdCheckBox_PFA.grid(row=3, column=7, columnspan=2, sticky='w')
        self.noiseScanCheckBox_PFA.grid(row=5, column=7, columnspan=2, sticky='w')
        self.discBumpScanCheckBox_PFA.grid(row=7, column=7, columnspan=2, sticky='w')
        self.mergedBumpScanCheckBox_PFA.grid(row=9, column=7, columnspan=2, sticky='w')
        self.retuneAndZeroBiasThreshScanCheckBox_PFA.grid(row=11, column=7, columnspan=2, sticky='w')
        self.sourceScanCheckBox_PFA.grid(row=13, column=7, columnspan=2, sticky='w')


class Yarr_Selection_Bar(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.borderFrame = ctk.CTkFrame(self, height=5, fg_color='#0d0b1e', corner_radius=2)
        self.borderFrame.grid(row=8,column=0,columnspan=11,sticky='esw')

        self.mhtButton = myTitleButton1(self,'#f5efed','#f5efed','#0d0b1e',100,30,"MHT",self.customFont,parent.switchToYarr, is_clicked=True)
        self.tunButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"TUN",self.customFont,parent.switchToMQT)
        self.pfaButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"PFA",self.customFont,parent.switchToMQAT)
        self.allTestsButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"All Tests",self.customFont,parent.switchToMQDT)
        
        self.mhtButton.other_buttons=[self.tunButton,self.pfaButton,self.allTestsButton]
        self.tunButton.other_buttons=[self.mhtButton,self.pfaButton,self.allTestsButton]
        self.pfaButton.other_buttons=[self.mhtButton,self.tunButton,self.allTestsButton]
        self.allTestsButton.other_buttons=[self.mhtButton,self.tunButton,self.pfaButton]
        
        self.mhtButton.grid(row=7,column=0,sticky='nesw')
        self.tunButton.grid(row=7,column=1,sticky='nesw')
        self.pfaButton.grid(row=7,column=2,sticky='nesw')
        self.allTestsButton.grid(row=7,column=3,sticky='nesw')
        
        self.mhtButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.mhtButton))
        self.mhtButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.mhtButton))

        self.tunButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.tunButton))
        self.tunButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.tunButton))

        self.pfaButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.pfaButton))
        self.pfaButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.pfaButton))

        self.allTestsButton.bind("<Enter>", lambda event: parent.onEnter1(event, self.allTestsButton))
        self.allTestsButton.bind("<Leave>", lambda event: parent.onLeave1(event, self.allTestsButton))




class Yarr_AllTests_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)

        self.TestFrameTitle = myLabel(self, "#0d0b1e", 100, 20, "YARR Tests", ctk.CTkFont("Roboto",25))
        self.TestFrame = Yarr_Test_Frame(self)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "|       Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.selectModuleLabel.grid(row=0, column=1, columnspan=4, sticky="w")
        self.moduleSelection.grid(row=0, column=2, columnspan=3)
        self.askForLocalDBLabel.grid(row=0, column=4, columnspan=3)
        self.askForLocalDB_Yes.grid(row=0, column=6, columnspan=3)
        self.askForLocalDB_No.grid(row=0, column=7, columnspan=3)

        #self.TestFrameTitle.grid(row=1, column=1)
        self.TestFrame.grid(row=1, column=1, columnspan=10, rowspan=5, sticky="nesw")

        self.runSelectMHTTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nMHT Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        self.runAllMHTTests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nMHT Tests", self.customFont,parent.moveToChip1, cornerRad=10)

        self.runSelectTUNTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nTUN Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        self.runAllTUNTests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nTUN Tests", self.customFont,parent.moveToChip1, cornerRad=10)

        self.runSelectPFATests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nPFA Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        self.runAllPFATests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nPFA Tests", self.customFont,parent.moveToChip1, cornerRad=10)


        self.runSelectMHTTests.grid(row=7, column=1, columnspan=2)
        self.runAllMHTTests.grid(row=8, column=1, columnspan=2)

        self.runSelectTUNTests.grid(row=7, column=4, columnspan=3)
        self.runAllTUNTests.grid(row=8, column=4, columnspan=3)

        self.runSelectPFATests.grid(row=7, column=8, columnspan=3)
        self.runAllPFATests.grid(row=8, column=8, columnspan=3)

        self.runAllYarrTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 500, 60, "Run All YARR Tests\n(without Source Scan)", self.customFont,parent.moveToChip1, cornerRad=10)

        self.runAllYarrTests.grid(row=9, column=0, columnspan=12)

class Yarr_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)



        
class MQT_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)


class MQAT_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)


class MQDT_Frame(ctk.CTkFrame):
    def	__init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont	= ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)


class FullQC_Frame(ctk.CTkFrame):
    def	__init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont	= ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8, 9, 10, 11, 12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)
        
class Interlocks_Control_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#0d0b1e', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)


class DCS_Switch_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#0d0b1e', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)

        self.LV_switch = mySwitch(self, text="LV Switch", text_color='#f5efed',switch_width=80,switch_height=30)
        self.LV_switch.grid(row=0, column=0, columnspan=8,sticky='nesw',padx=5)

        self.HV_switch = mySwitch(self, text="HV Switch", text_color='#f5efed',switch_width=80,switch_height=30)
        self.HV_switch.grid(row=3, column=0, columnspan=8,sticky='nesw',padx=5)

        self.Peltier_switch = mySwitch(self, text="Peltier Switch", text_color='#f5efed', switch_width=80, switch_height=30)
        self.Peltier_switch.grid(row=6, column=0, columnspan=8, sticky='nesw', padx=5)

        self.Chiller_switch = mySwitch(self, text="Chiller Switch", text_color='#f5efed', switch_width=80, switch_height=30)
        self.Chiller_switch.grid(row=9, column=0, columnspan=8, sticky='nesw', padx=5)



class SourceControl_Button_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#0d0b1e', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)

        self.moveToChip1Button = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 150, 150, "Press\nTo Move\nSource To\nChip 1", self.customFont,parent.moveToChip1)
        self.moveToChip2Button = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 150, 150, "Press\nTo Move\nSource To\nChip 2", self.customFont,parent.moveToChip1)
        self.moveToChip3Button = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 150, 150, "Press\nTo Move\nSource To\nChip 3", self.customFont,parent.moveToChip1)
        self.moveToChip4Button = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 150, 150, "Press\nTo Move\nSource To\nChip 4", self.customFont,parent.moveToChip1)
        self.returnSource = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 300, 70, "Press to Return\nSource to Cradle", self.customFont,parent.moveToChip1)
        self.moveToCenterButton = myButton(self,'#61d095', '#2f9d62', '#0d0b1e', 300, 70, "Press To Move\nSource To Center", self.customFont,parent.moveToChip1)

        #self.moveToChip1Button.place(relx=0.27, rely=0.27, anchor=tkinter.CENTER)
        #self.moveToChip2Button.place(relx=0.27, rely=0.6, anchor=tkinter.CENTER)
        #self.moveToChip3Button.place(relx=0.73, rely=0.6, anchor=tkinter.CENTER)
        #self.moveToChip4Button.place(relx=0.73, rely=0.27, anchor=tkinter.CENTER)
        #self.moveToCenterButton.place(relx=0.5, rely=0.435, anchor=tkinter.CENTER)
        #self.returnSource.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        
        self.moveToChip1Button.grid(row=5, column=5, padx=1, pady=1)
        self.moveToChip2Button.grid(row=6, column=5, padx=1, pady=1)
        self.moveToChip3Button.grid(row=6, column=6, padx=1, pady=1)
        self.moveToChip4Button.grid(row=5, column=6, padx=1, pady=1)
        self.moveToCenterButton.grid(row=7, column=5, columnspan=2, padx=10)
        self.returnSource.grid(row=10, column=5, columnspan=2, padx=10)


class DCS_Title_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#0d0b1e', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)


        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.InterlocksButton = myTitleButton2(self,'#0d0b1e', '#0d0b1e', '#f5efed', 100, 30, "Interlocks", self.customFont, parent.switchToInterlocks, is_clicked=True)
        self.InterlocksButton.grid(row=7,column=0,sticky="nesw",padx=10)

        self.DCSSwitchesButton = myTitleButton2(self,'#0d0b1e','#0d0b1e','#666666',100,30,"DCS",self.customFont,parent.switchToDCSButtons)
        self.DCSSwitchesButton.grid(row=7,column=1,sticky="nesw",padx=10)

        self.SourceControlButton = myTitleButton2(self, '#0d0b1e', '#0d0b1e', '#666666', 130, 30, "Source\nControl",self.customFont,parent.switchToSourceControl) #d6d1cd
        self.SourceControlButton.grid(row=7,column=2,sticky='nesw',padx=10)
        
        self.InterlocksButton.other_buttons=[self.DCSSwitchesButton,self.SourceControlButton]
        self.DCSSwitchesButton.other_buttons=[self.SourceControlButton,self.InterlocksButton]
        self.SourceControlButton.other_buttons=[self.DCSSwitchesButton,self.InterlocksButton]

        self.DCSSwitchesButton.bind("<Enter>", lambda event: parent.onEnter2(event, self.DCSSwitchesButton))
        self.DCSSwitchesButton.bind("<Leave>", lambda event: parent.onLeave2(event, self.DCSSwitchesButton))

        self.SourceControlButton.bind("<Enter>", lambda event: parent.onEnter2(event, self.SourceControlButton))
        self.SourceControlButton.bind("<Leave>", lambda event: parent.onLeave2(event, self.SourceControlButton))

        self.InterlocksButton.bind("<Enter>", lambda event: parent.onEnter2(event, self.InterlocksButton))
        self.InterlocksButton.bind("<Leave>", lambda event: parent.onLeave2(event, self.InterlocksButton))
        
        self.borderFrame = ctk.CTkFrame(self, height=5, fg_color='#f5efed', corner_radius=2)
        self.borderFrame.grid(row=8,column=0,columnspan=11, sticky='esw')




class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#f5efed')

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        

        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        self.geometry("1750x900")
        self.minsize(1750,900)
        self.title("AMAF Electrical Testing")
        self.resizable(True,True)

        self.selectionBar = Selection_Bar(parent=self)
        self.selectionBar.grid(row=0,column=1,columnspan=5, sticky='nesw')

        self.interlocksControlFrame = Interlocks_Control_Frame(parent=self)
        self.interlocksControlFrame.grid(row=1,column=0,rowspan=5, sticky='nesw')

        self.dcsTitleFrame = DCS_Title_Frame(parent=self)
        self.dcsTitleFrame.grid(row=0,column=0, sticky='nesw')

        self.dcsSwitchFrame = DCS_Switch_Frame(parent=self)

        self.sourceControlFrame = SourceControl_Button_Frame(parent=self)

        self.yarrFrame = Yarr_Frame(parent=self)
        self.mqtFrame = MQT_Frame(parent=self)
        self.mqatFrame = MQAT_Frame(parent=self)
        self.mqdtFrame = MQDT_Frame(parent=self)
        self.fullqcFrame = FullQC_Frame(parent=self)
        
        self.yarrFrame.grid(row=1,column=1, rowspan=5, columnspan=5, sticky='nesw')

    def switchToInterlocks(self):
        self.dcsSwitchFrame.grid_forget()
        self.sourceControlFrame.grid_forget()
        self.interlocksControlFrame.grid(row=1, column=0, rowspan=5, sticky='nesw')

    def switchToDCSButtons(self):
        self.sourceControlFrame.grid_forget()
        self.interlocksControlFrame.grid_forget()
        self.dcsSwitchFrame.grid(row=1, column=0, rowspan=5, sticky='nesw')

    def switchToSourceControl(self):
        self.dcsSwitchFrame.grid_forget()
        self.interlocksControlFrame.grid_forget()
        self.sourceControlFrame.grid(row=1, column=0, rowspan=5, sticky='nesw')

    def switchToYarr(self):
        self.mqtFrame.grid_forget()
        self.mqatFrame.grid_forget()
        self.mqdtFrame.grid_forget()
        self.fullqcFrame.grid_forget()
        self.yarrFrame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky='nesw')
        return
    
    def switchToMQT(self):
        self.yarrFrame.grid_forget()
        self.mqatFrame.grid_forget()
        self.mqdtFrame.grid_forget()
        self.fullqcFrame.grid_forget()
        self.mqtFrame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky='nesw')

    def switchToMQAT(self):
        self.yarrFrame.grid_forget()
        self.mqtFrame.grid_forget()
        self.mqdtFrame.grid_forget()
        self.fullqcFrame.grid_forget()
        self.mqatFrame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky='nesw')

    def switchToMQDT(self):
        self.yarrFrame.grid_forget()
        self.mqtFrame.grid_forget()
        self.mqatFrame.grid_forget()
        self.fullqcFrame.grid_forget()
        self.mqdtFrame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky='nesw')

    def switchToFullQC(self):
        self.yarrFrame.grid_forget()
        self.mqtFrame.grid_forget()
        self.mqatFrame.grid_forget()
        self.mqdtFrame.grid_forget()
        self.fullqcFrame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky='nesw')


    def onEnter1(self,event, custom_button):
        self.configure(fg_color="#f5efed")
        if not custom_button.is_clicked:
            custom_button.button.configure(text_color='#0d0b1e')

    def onEnter2(self,event, custom_button):
        self.configure(fg_color="#0d0b1e")
        if not custom_button.is_clicked:
            custom_button.button.configure(text_color='#f5efed')

    def onLeave1(self,event, custom_button):
        if not custom_button.is_clicked:
            custom_button.button.configure(text_color='#d6d1cd')

    def onLeave2(self,event, custom_button):
        if not custom_button.is_clicked:
            custom_button.button.configure(text_color='#666666')

    def moveToChip1(self):
        return
    

app = App()
app.mainloop()
