import tkinter
import customtkinter as ctk # <- import the CustomTkinter module 
from customWidgets import *                                                                                                               
from tkinter import filedialog 
from statistics import mean
import numpy as np
import os
import os.path
import subprocess
from datetime import datetime
from functools import reduce
import time


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

class Yarr_MHT_Frame(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):

        self.app = app
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)
        self.buttonFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)
        self.selectModuleLabel.grid(row=0,column=3,sticky='w')
        self.moduleSelection.grid(row=0,column=4)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "  |  Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.askForLocalDBLabel.grid(row=0,column=5,sticky='w')
        self.askForLocalDB_Yes.grid(row=0,column=6)
        self.askForLocalDB_No.grid(row=0,column=7)

        self.eyeDiagramLabel = myLabel(self, "#0d0b1e", 100, 30, "1. Eye Diagram ", self.customFont)
        self.eyeArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.eyeDiagramLabel.grid(row=1,column=3,sticky='w')
        self.eyeArrow.grid(row=1,column=4)

        self.digitalScanLabel = myLabel(self, '#0d0b1e', 100,30,"2. Digital Scan ", self.customFont)
        self.digArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.digitalScanLabel.grid(row=2,column=3,sticky='w')
        self.digArrow.grid(row=2,column=4)

        self.analogScanLabel = myLabel(self, '#0d0b1e', 100, 30, "3. Analog Scan ", self.customFont)
        self.anaArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.analogScanLabel.grid(row=3,column=3,sticky='w')
        self.anaArrow.grid(row=3,column=4)

        self.threshScanHrLabel = myLabel(self, '#0d0b1e', 100, 30, "4. Threshold Scan HR ", self.customFont)
        self.threshArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.threshScanHrLabel.grid(row=4,column=3,sticky='w')
        self.threshArrow.grid(row=4,column=4)

        self.totScanLabel = myLabel(self, '#0d0b1e', 100, 30, "5. TOT Scan ", self.customFont)
        self.totArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.totScanLabel.grid(row=5,column=3,sticky='w')
        self.totArrow.grid(row=5,column=4)

        self.runEyeButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nEye Diagram", self.buttonFont,self.runEyeFunc, cornerRad=10)
        self.runEyeButton.grid(row=1, column=5, columnspan=3)

        self.runDigButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nDigital Scan", self.buttonFont,self.runDigFunc, cornerRad=10)
        self.runDigButton.grid(row=2, column=5, columnspan=3)

        self.runAnaButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nAnalog Scan", self.buttonFont,self.runAnaFunc, cornerRad=10)
        self.runAnaButton.grid(row=3, column=5, columnspan=3)

        self.runThreshButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nThreshold Scan HR", self.buttonFont,self.runThreshFunc, cornerRad=10)
        self.runThreshButton.grid(row=4, column=5, columnspan=3)

        self.runTotButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nTOT Scan", self.buttonFont,self.runTotFunc, cornerRad=10)
        self.runTotButton.grid(row=5, column=5, columnspan=3)

    def runEyeFunc(self):
        self.app.runEyeMHT()
    
    def runDigFunc(self):
        self.app.runDigMHT()

    def runAnaFunc(self):
        self.app.runAnaMHT()

    def runThreshFunc(self):
        self.app.runThreshMHT()

    def runTotFunc(self):
        self.app.runTotMHT()

    def runAllFunc(self):
        self.app.runAllMHT()

class Yarr_TUN_Frame(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):

        self.app = app
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)
        self.buttonFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)
        self.selectModuleLabel.grid(row=0,column=3,sticky='w')
        self.moduleSelection.grid(row=0,column=4)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "  |  Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.askForLocalDBLabel.grid(row=0,column=5,sticky='w')
        self.askForLocalDB_Yes.grid(row=0,column=6)
        self.askForLocalDB_No.grid(row=0,column=7)

        self.clearChipConfigLabel = myLabel(self, "#f8333c", 100, 30, "1. Clear Chip Config ", self.customFont)
        self.clearChipConfigArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.clearChipConfigLabel.grid(row=1,column=3,sticky='w')
        self.clearChipConfigArrow.grid(row=1,column=4)

        self.threshScanHrLabel = myLabel(self, '#0d0b1e', 100,30,"2. Threshold Scan HR ", self.customFont)
        self.threshHrArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.threshScanHrLabel.grid(row=2,column=3,sticky='w')
        self.threshHrArrow.grid(row=2,column=4)

        self.preTotScanLabel = myLabel(self, '#0d0b1e', 100, 30, "3. Pre-Tune TOT Scan ", self.customFont)
        self.preTotArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.preTotScanLabel.grid(row=3,column=3,sticky='w')
        self.preTotArrow.grid(row=3,column=4)

        self.tuneGlobalThreshLabel = myLabel(self, '#0d0b1e', 100, 30, "4. Tune Global Threshold ", self.customFont)
        self.tuneGlobalThreshArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.tuneGlobalThreshLabel.grid(row=4,column=3,sticky='w')
        self.tuneGlobalThreshArrow.grid(row=4,column=4)

        self.tunePixelThreshLabel = myLabel(self, '#0d0b1e', 100, 30, "5. Tune Pixel Threshold ", self.customFont)
        self.tunePixelThreshArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.tunePixelThreshLabel.grid(row=5,column=3,sticky='w')
        self.tunePixelThreshArrow.grid(row=5,column=4)

        self.threshScanHdLabel = myLabel(self, '#0d0b1e', 100,30,"6. Threshold Scan HD ", self.customFont)
        self.threshHdArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.threshScanHdLabel.grid(row=6,column=3,sticky='w')
        self.threshHdArrow.grid(row=6,column=4)

        self.postTotScanLabel = myLabel(self, '#0d0b1e', 100, 30, "7. Post-Tune TOT Scan ", self.customFont)
        self.postTotArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.postTotScanLabel.grid(row=7,column=3,sticky='w')
        self.postTotArrow.grid(row=7,column=4)

        self.clearChipConfigButton = myButton(self,'#f8333c','#c50711', '#0d0b1e', 200, 60, "Clear Chip Config", self.buttonFont,self.clearChipConfigFunc, cornerRad=10)
        self.clearChipConfigButton.grid(row=1, column=5, columnspan=3)

        self.runThreshHrButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nThreshold Scan HR", self.buttonFont,self.runThreshHrFunc, cornerRad=10)
        self.runThreshHrButton.grid(row=2, column=5, columnspan=3)

        self.runPreTotButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Pre-Tune\nTOT Scan", self.buttonFont,self.runPreTotFunc, cornerRad=10)
        self.runPreTotButton.grid(row=3, column=5, columnspan=3)

        self.tuneGlobalThreshButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Tune Global\nThreshold", self.buttonFont,self.tuneGlobalThreshFunc, cornerRad=10)
        self.tuneGlobalThreshButton.grid(row=4, column=5, columnspan=3)

        self.tunePixelThreshButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Tune Pixel\nThreshold", self.buttonFont,self.tunePixelThreshFunc, cornerRad=10)
        self.tunePixelThreshButton.grid(row=5, column=5, columnspan=3)

        self.runThreshHdButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nThreshold Scan HD", self.buttonFont,self.runThreshHdFunc, cornerRad=10)
        self.runThreshHdButton.grid(row=6, column=5, columnspan=3)

        self.runPostTotButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Post-Tune\nTOT Scan", self.buttonFont,self.runPostTotFunc, cornerRad=10)
        self.runPostTotButton.grid(row=7, column=5, columnspan=3)

    def clearChipConfigFunc(self):
        self.app.clearChipConfigTUN()

    def runThreshHrFunc(self):
        self.app.runThreshHrTUN()

    def runPreTotFunc(self):
        self.app.runPreTotScanTUN()

    def tuneGlobalThreshFunc(self):
        self.app.tuneGlobalThreshTUN()

    def tunePixelThreshFunc(self):
        self.app.tunePixelThreshTUN()

    def runThreshHdFunc(self):
        self.app.runThreshHdTUN()

    def runPostTotFunc(self):
        self.app.runPostTotScanTUN()

class Yarr_PFA_Frame(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):

        self.app = app
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)
        self.buttonFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)
        self.selectModuleLabel.grid(row=0,column=3,sticky='w')
        self.moduleSelection.grid(row=0,column=4)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "  |  Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.askForLocalDBLabel.grid(row=0,column=5,sticky='w')
        self.askForLocalDB_Yes.grid(row=0,column=6)
        self.askForLocalDB_No.grid(row=0,column=7)

        self.digitalScanLabel = myLabel(self, '#0d0b1e', 100,30,"1. Digital Scan ", self.customFont)
        self.digArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.digitalScanLabel.grid(row=1,column=3,sticky='w')
        self.digArrow.grid(row=1,column=4)

        self.analogScanLabel = myLabel(self, '#0d0b1e', 100, 30, "2. Analog Scan ", self.customFont)
        self.anaArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.analogScanLabel.grid(row=2,column=3,sticky='w')
        self.anaArrow.grid(row=2,column=4)

        self.threshScanHdLabel = myLabel(self, '#0d0b1e', 100, 30, "3. Threshold Scan HD ", self.customFont)
        self.threshHdArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.threshScanHdLabel.grid(row=3,column=3,sticky='w')
        self.threshHdArrow.grid(row=3,column=4)

        self.noiseScanLabel = myLabel(self, '#0d0b1e', 100, 30, "4. Noise Scan ", self.customFont)
        self.noiseScanArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.noiseScanLabel.grid(row=4,column=3,sticky='w')
        self.noiseScanArrow.grid(row=4,column=4)

        self.discBumpScanLabel = myLabel(self, '#0d0b1e', 100, 30, "5. Disconnected Bump Scan ", self.customFont)
        self.discBumpScanArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.discBumpScanLabel.grid(row=5,column=3,sticky='w')
        self.discBumpScanArrow.grid(row=5,column=4)

        self.mergedBumpScanLabel = myLabel(self, '#0d0b1e', 100, 30, "6. Merged Bump Scan ", self.customFont)
        self.mergedBumpScanArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.mergedBumpScanLabel.grid(row=6,column=3,sticky='w')
        self.mergedBumpScanArrow.grid(row=6,column=4)

        self.reTune_ZeroBias_ResetLabel = myLabel(self, '#0d0b1e', 100, 30, 
                                                  "7. Retune Pixel Threshold/\nZero Bias Thresh. Scan/\nReset Chip Configs",
                                                  self.customFont)
        self.reTune_ZeroBias_ResetArrow = myLabel(self, "#0d0b1e", 100, 30, "-------------------------> ", self.customFont)
        self.reTune_ZeroBias_ResetLabel.grid(row=7,column=3,sticky='w')
        self.reTune_ZeroBias_ResetArrow.grid(row=7,column=4)

        self.sourceScanLabel = myLabel(self, '#f8333c', 100, 30, "8. 50 min. Source Scan ", self.customFont)
        self.sourceScanArrow = myLabel(self, '#0d0b1e', 100, 30, "-------------------------> ", self.customFont)
        self.sourceScanLabel.grid(row=8, column=3, sticky='w')
        self.sourceScanArrow.grid(row=8, column=4, sticky='w')

        self.runDigButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nDigital Scan", self.buttonFont,self.runDigFunc, cornerRad=10)
        self.runDigButton.grid(row=1, column=5, columnspan=3)

        self.runAnaButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nAnalog Scan", self.buttonFont,self.runAnaFunc, cornerRad=10)
        self.runAnaButton.grid(row=2, column=5, columnspan=3)

        self.runThreshButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nThreshold Scan HD", self.buttonFont,self.runThreshFunc, cornerRad=10)
        self.runThreshButton.grid(row=3, column=5, columnspan=3)

        self.runNoiseScanButton = myButton(self,'#ffd449','#e0ac00' , '#0d0b1e', 200, 60, "Run\nNoise Scan", self.buttonFont,self.runNoiseScanFunc, cornerRad=10)
        self.runNoiseScanButton.grid(row=4, column=5, columnspan=3)

        self.runDiscScanButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nDisconnected Bump Scan", self.buttonFont,self.runDiscBumpFunc, cornerRad=10)
        self.runDiscScanButton.grid(row=5, column=5, columnspan=3)

        self.runMergedScanButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run\nMerged Bump Scan", self.buttonFont,self.runMergedBumpFunc, cornerRad=10)
        self.runMergedScanButton.grid(row=6, column=5, columnspan=3)

        self.runZeroBiasScanButton = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Zero Bias\nThreshold Scan", self.buttonFont,self.runZeroBiasFunc, cornerRad=10)
        self.runZeroBiasScanButton.grid(row=7, column=5, columnspan=3)

        self.runSourceScanButton = myButton(self,'#f8333c','#c50711', '#0d0b1e', 200, 60, "Run\n50 min. Source Scan", self.buttonFont,self.runSourceFunc, cornerRad=10)
        self.runSourceScanButton.grid(row=8, column=5, columnspan=3)

    def runDigFunc(self):
        self.app.runDigPFA()

    def runAnaFunc(self):
        self.app.runAnaPFA()

    def runThreshFunc(self):
        self.app.runThreshPFA()
    
    def runNoiseScanFunc(self):
        self.app.runNoiseScanPFA()

    def runDiscBumpFunc(self):
        self.app.runDiscBumpScanPFA()

    def runMergedBumpFunc(self):
        self.app.runMergedBumpScanPFA()

    def runZeroBiasFunc(self):
        self.app.runZeroBiasPFA()

    def runSourceFunc(self):
        self.app.runSourceScan()

class Yarr_Selection_Bar(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):

        self.app = app
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",25)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.mhtButton = myTitleButton1(self,'#f5efed','#f5efed','#0d0b1e',100,30,"MHT",self.customFont,self.mhtButtonFunction, is_clicked=True)
        self.divider1 = myLabel(self,'#d6d1cd',20,30,"|",self.customFont)
        self.tunButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"TUN",self.customFont,self.tunButtonFunction)
        self.divider2 = myLabel(self,'#d6d1cd',20,30,"|",self.customFont)
        self.pfaButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"PFA",self.customFont,self.pfaButtonFunction)
        self.divider3 = myLabel(self,'#d6d1cd',20,30,"|",self.customFont)
        self.allTestsButton = myTitleButton1(self,'#f5efed','#f5efed','#d6d1cd',100,30,"All Tests",self.customFont,self.allTestsButtonFunction)
        
        self.mhtButton.other_buttons=[self.tunButton,self.pfaButton,self.allTestsButton]
        self.tunButton.other_buttons=[self.mhtButton,self.pfaButton,self.allTestsButton]
        self.pfaButton.other_buttons=[self.mhtButton,self.tunButton,self.allTestsButton]
        self.allTestsButton.other_buttons=[self.mhtButton,self.tunButton,self.pfaButton]
        
        self.mhtButton.grid(row=0,column=0,sticky='nesw')
        self.divider1.grid(row=0,column=1)
        self.tunButton.grid(row=0,column=2,sticky='nesw')
        self.divider2.grid(row=0,column=3)
        self.pfaButton.grid(row=0,column=4,sticky='nesw')
        self.divider3.grid(row=0,column=5)
        self.allTestsButton.grid(row=0,column=6,sticky='nesw')
        
        self.mhtButton.bind("<Enter>", lambda event: self.app.onEnter1(event, self.mhtButton))
        self.mhtButton.bind("<Leave>", lambda event: self.app.onLeave1(event, self.mhtButton))

        self.tunButton.bind("<Enter>", lambda event: self.app.onEnter1(event, self.tunButton))
        self.tunButton.bind("<Leave>", lambda event: self.app.onLeave1(event, self.tunButton))

        self.pfaButton.bind("<Enter>", lambda event: self.app.onEnter1(event, self.pfaButton))
        self.pfaButton.bind("<Leave>", lambda event: self.app.onLeave1(event, self.pfaButton))

        self.allTestsButton.bind("<Enter>", lambda event: self.app.onEnter1(event, self.allTestsButton))
        self.allTestsButton.bind("<Leave>", lambda event: self.app.onLeave1(event, self.allTestsButton))

    def mhtButtonFunction(self):
        self.app.switchToMHT()
    def tunButtonFunction(self):
        self.app.switchToTUN()
    def pfaButtonFunction(self):
        self.app.switchToPFA()
    def allTestsButtonFunction(self):
        self.app.switchToAllTests()
        
class Yarr_AllTests_Frame(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)
        self.buttonFont = ctk.CTkFont("Roboto",20)

        self.app=app

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)
        self.selectModuleLabel.grid(row=0,column=3,sticky='w')
        self.moduleSelection.grid(row=0,column=4)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "  |  Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.askForLocalDBLabel.grid(row=0,column=5,sticky='w')
        self.askForLocalDB_Yes.grid(row=0,column=6)
        self.askForLocalDB_No.grid(row=0,column=7)

        self.allMHTsLabel = myLabel(self, '#0d0b1e', 100,30,"Run All MHT Scans ", self.customFont)
        self.allMHTsArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.allMHTsLabel.grid(row=1,column=3,sticky='w')
        self.allMHTsArrow.grid(row=1,column=4)

        self.allTUNsLabel = myLabel(self, '#0d0b1e', 100,30,"Run All TUN Scans ", self.customFont)
        self.allTUNsArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.allTUNsLabel.grid(row=2,column=3,sticky='w')
        self.allTUNsArrow.grid(row=2,column=4)

        self.allPFAsLabel = myLabel(self, '#0d0b1e', 100,30,"Run All PFA Scans ", self.customFont)
        self.allPFAsArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.allPFAsArrowSplit = myLabel(self, "#0d0b1e", 100, 30, "|", ctk.CTkFont("Roboto",45))
        self.allPFAsArrowSplit2 = myLabel(self, "#0d0b1e", 100, 30, "|", ctk.CTkFont("Roboto",45))
        self.allPFAsArrow2 = myLabel(self, "#0d0b1e", 100,30,"---------------->", self.customFont)
        self.allPFAsLabel.grid(row=3,column=3,sticky='w')
        self.allPFAsArrow.grid(row=3,column=4)
        self.allPFAsArrowSplit.grid(row=3,column=4,sticky="s")
        self.allPFAsArrowSplit2.grid(row=4, column=4,sticky='n')
        self.allPFAsArrow2.grid(row=4, column=4, sticky='e')

        self.runMhtButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nMHT Scans ", self.buttonFont,self.runMhtFunc, cornerRad=10)
        self.runMhtButton.grid(row=1, column=5, columnspan=3)

        self.runTunButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nTUN Scans ", self.buttonFont,self.runTunFunc, cornerRad=10)
        self.runTunButton.grid(row=2, column=5, columnspan=3)

        self.runPfaNoSourceButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nPFA Scans\n(Without Source Scan)", self.buttonFont,self.runPfaNoSourceFunc, cornerRad=10)
        self.runPfaNoSourceButton.grid(row=3, column=5, columnspan=3)

        self.runPfaWithSourceButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nPFA Scans\n(With Source Scan)", self.buttonFont,self.runPfaWithSourceFunc, cornerRad=10)
        self.runPfaWithSourceButton.grid(row=4, column=5, columnspan=3)

    def runMhtFunc(self):
        self.app.runAllMHT()

    def runTunFunc(self):
        self.app.runAllTUN()

    def runPfaNoSourceFunc(self):
        self.app.runAllPfaNoSource()

    def runPfaWithSourceFunc(self):
        self.app.runAllPfaWithSource()

        
        #self.TestFrame = Yarr_Test_Frame(self)


        #self.TestFrameTitle.grid(row=1, column=1)
        #self.TestFrame.grid(row=1, column=1, columnspan=10, rowspan=5, sticky="nesw")

        #self.runSelectMHTTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nMHT Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        #self.runAllMHTTests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nMHT Tests", self.customFont,parent.moveToChip1, cornerRad=10)

        #self.runSelectTUNTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nTUN Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        #self.runAllTUNTests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nTUN Tests", self.customFont,parent.moveToChip1, cornerRad=10)

        #self.runSelectPFATests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 200, 60, "Run Selected\nPFA Tests", self.customFont,parent.moveToChip1, cornerRad=10)
        #self.runAllPFATests = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run All\nPFA Tests", self.customFont,parent.moveToChip1, cornerRad=10)


        #self.runSelectMHTTests.grid(row=7, column=1, columnspan=2)
        #self.runAllMHTTests.grid(row=8, column=1, columnspan=2)

        #self.runSelectTUNTests.grid(row=7, column=4, columnspan=3)
        #self.runAllTUNTests.grid(row=8, column=4, columnspan=3)

        #self.runSelectPFATests.grid(row=7, column=8, columnspan=3)
        #self.runAllPFATests.grid(row=8, column=8, columnspan=3)

        #self.runAllYarrTests = myButton(self,'#ffd449','#e0ac00', '#0d0b1e', 500, 60, "Run All YARR Tests\n(without Source Scan)", self.customFont,parent.moveToChip1, cornerRad=10)

        #self.runAllYarrTests.grid(row=9, column=0, columnspan=12)

class Yarr_Frame(ctk.CTkFrame):
    def __init__(self, parent, app, **kwargs):

        self.app = app
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)

        self.selectionBar = Yarr_Selection_Bar(parent=self, app=app)
        self.selectionBar.grid(row=0,column=0, sticky='nesw')

        self.mhtFrame = Yarr_MHT_Frame(parent=self, app=app)
        self.mhtFrame.grid(row=1,column=0, rowspan=5, sticky='nesw')

        self.tunFrame = Yarr_TUN_Frame(parent=self, app=app)

        self.pfaFrame = Yarr_PFA_Frame(parent=self, app=app)

        self.allTestsFrame = Yarr_AllTests_Frame(parent=self,app=app)

class MQT_Frame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color='#f5efed', corner_radius=2, **kwargs)

        self.customFont = ctk.CTkFont("Roboto",30)
        self.buttonFont = ctk.CTkFont("Roboto",20)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.selectModuleLabel = myLabel(self, "#0d0b1e", 100, 20, "Please select Module: ", self.customFont)
        self.moduleSelection = ctk.CTkOptionMenu(self,values=["ANL_ITkPix_"+str(i) for i in range(1,46)],font=self.customFont)
        self.selectModuleLabel.grid(row=0,column=3,sticky='w')
        self.moduleSelection.grid(row=0,column=4)

        self.askForLocalDBLabel = myLabel(self, "#0d0b1e", 100, 20, "  |  Upload to Local DB?: ", self.customFont)
        self.askForLocalDBVar = tkinter.IntVar(value=0)
        self.askForLocalDB_Yes = ctk.CTkRadioButton(self, text="Yes", variable=self.askForLocalDBVar, value=1, font=self.customFont)
        self.askForLocalDB_No = ctk.CTkRadioButton(self, text="No", variable=self.askForLocalDBVar, value=0, font=self.customFont)

        self.askForLocalDBLabel.grid(row=0,column=5,sticky='w')
        self.askForLocalDB_Yes.grid(row=0,column=6)
        self.askForLocalDB_No.grid(row=0,column=7)

        self.ivLabel = myLabel(self, "#0d0b1e", 100, 30, "1. IV Measure ", self.customFont)
        self.ivArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.ivLabel.grid(row=1,column=3,sticky='w')
        self.ivArrow.grid(row=1,column=4)

        self.adcLabel = myLabel(self, "#0d0b1e", 100, 30, "2. ADC Calibration ", self.customFont)
        self.adcArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.adcLabel.grid(row=2,column=3,sticky='w')
        self.adcArrow.grid(row=2,column=4)

        self.anaReadBackLabel = myLabel(self, "#0d0b1e", 100, 30, "3. Analog Readback ", self.customFont)
        self.anaReadBackArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.anaReadBackLabel.grid(row=3,column=3,sticky='w')
        self.anaReadBackArrow.grid(row=3,column=4)

        self.sldoLabel = myLabel(self, "#0d0b1e", 100, 30, "4. SLDO ", self.customFont)
        self.sldoArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.sldoLabel.grid(row=4,column=3,sticky='w')
        self.sldoArrow.grid(row=4,column=4)

        self.vCalLabel = myLabel(self, "#0d0b1e", 100, 30, "5. VCAL Calibration ", self.customFont)
        self.vCalArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.vCalLabel.grid(row=5,column=3,sticky='w')
        self.vCalArrow.grid(row=5,column=4)

        self.dataTransmissionLabel = myLabel(self, "#0d0b1e", 100, 30, "6. Data Transmission ", self.customFont)
        self.dataTransmissionArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.dataTransmissionLabel.grid(row=6,column=3,sticky='w')
        self.dataTransmissionArrow.grid(row=6,column=4)

        self.injectCapLabel = myLabel(self, "#0d0b1e", 100, 30, "7. Injection Capacitance ", self.customFont)
        self.injectCapArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.injectCapLabel.grid(row=7,column=3,sticky='w')
        self.injectCapArrow.grid(row=7,column=4)

        self.lpLabel = myLabel(self, "#0d0b1e", 100, 30, "8. Low Power Mode ", self.customFont)
        self.lpArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.lpLabel.grid(row=8,column=3,sticky='w')
        self.lpArrow.grid(row=8,column=4)

        self.ovpLabel = myLabel(self, "#0d0b1e", 100, 30, "9. Over-Voltage Protection ", self.customFont)
        self.ovpArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.ovpLabel.grid(row=9,column=3,sticky='w')
        self.ovpArrow.grid(row=9,column=4)

        self.underShuntLabel = myLabel(self, "#0d0b1e", 100, 30, "10. Undershunt Protection ", self.customFont)
        self.underShuntArrow = myLabel(self, "#0d0b1e", 100, 30, "---------------------------------> ", self.customFont)
        self.underShuntLabel.grid(row=10,column=3,sticky='w')
        self.underShuntArrow.grid(row=10,column=4)

        self.runIvButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nIV Scan ", self.buttonFont,parent.runIV, cornerRad=10)
        self.runIvButton.grid(row=1, column=5, columnspan=3)

        self.runAdcButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nADC Calibration ", self.buttonFont,parent.runADC, cornerRad=10)
        self.runAdcButton.grid(row=2, column=5, columnspan=3)

        self.runArButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nAnalog Readback ", self.buttonFont,parent.runAnalogReadback, cornerRad=10)
        self.runArButton.grid(row=3, column=5, columnspan=3)

        self.runSldoButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nSLDO ", self.buttonFont,parent.runSLDO, cornerRad=10)
        self.runSldoButton.grid(row=4, column=5, columnspan=3)

        self.runVcalButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nVCAL Calibration ", self.buttonFont,parent.runVcal, cornerRad=10)
        self.runVcalButton.grid(row=5, column=5, columnspan=3)

        self.runDataTransButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nData Transmission", self.buttonFont,parent.runDataTrans, cornerRad=10)
        self.runDataTransButton.grid(row=6, column=5, columnspan=3)

        self.runInjectCapButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nInjection Capacitance", self.buttonFont,parent.runInjectCap, cornerRad=10)
        self.runInjectCapButton.grid(row=7, column=5, columnspan=3)

        self.runLpButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nLow Power Mode", self.buttonFont,parent.runLP, cornerRad=10)
        self.runLpButton.grid(row=8, column=5, columnspan=3)

        self.runOvpButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nOver-Voltage Protection", self.buttonFont,parent.runOVP, cornerRad=10)
        self.runOvpButton.grid(row=9, column=5, columnspan=3)

        self.runUnderShuntButton = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 200, 60, "Run\nUndershunt Protection", self.buttonFont,parent.runUndershunt, cornerRad=10)
        self.runUnderShuntButton.grid(row=10, column=5, columnspan=3)

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
        self.titleFont = ctk.CTkFont("Roboto",25)

        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight=1)

        self.lvTitle = myLabel(self, "#f5efed", 100, 20, "Low Voltage", self.titleFont)
        self.lvUnderscore = myLabel(self, "#f5efed", 100, 1, "----------------------", self.titleFont, fg_color='transparent')
        self.hvTitle = myLabel(self, '#f5efed', 100, 20, "High Voltage", self.titleFont)
        self.hvUnderscore = myLabel(self, "#f5efed", 100, 1, "----------------------", self.titleFont, fg_color='transparent')
        self.peltierTitle =  myLabel(self, '#f5efed', 100, 10, "Peltier", self.titleFont)
        self.peltierUnderscore = myLabel(self, "#f5efed", 100, 1, "-----------------------", self.titleFont, fg_color='transparent')
        self.chillerTitle = myLabel(self, '#f5efed', 100, 10, "Chiller", self.titleFont)
        self.chillerUnderscore = myLabel(self, "#f5efed", 100, 1, "----------------------", self.titleFont, fg_color='transparent')

        self.lvTitle.grid(row=0, column=0, sticky="nw", padx=15)
        self.lvUnderscore.grid(row=0, column=0, sticky='sw', padx=15)
        self.hvTitle.grid(row=3, column=0, sticky='nw', padx=15)
        self.hvUnderscore.grid(row=3,column=0, sticky='sw', padx=15)
        self.peltierTitle.grid(row=6, column=0, sticky='nw')
        self.peltierUnderscore.grid(row=6, column=0, sticky='sw', padx=15)
        self.chillerTitle.grid(row=9, column=0, sticky='nw')
        self.chillerUnderscore.grid(row=9, column=0, sticky='sw', padx=15)

        self.LV_switch = mySwitch(self, text="LV Switch", text_color='#f5efed',switch_width=80,switch_height=30)
        self.HV_switch = mySwitch(self, text="HV Switch", text_color='#f5efed',switch_width=80,switch_height=30)
        self.Peltier_switch = mySwitch(self, text="Peltier Switch", text_color='#f5efed', switch_width=80, switch_height=30)
        self.Chiller_switch = mySwitch(self, text="Chiller Switch", text_color='#f5efed', switch_width=80, switch_height=30)

        self.lvSwitchOn = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 80, 30, "On", self.customFont, functCommand=None, cornerRad=2)
        self.lvSwitchOff = myButton(self,'#f8333c','#c50711', '#0d0b1e', 80, 30, "Off", self.customFont, functCommand=None, cornerRad=2)
        
        self.hvSwitchOn = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 80, 30, "On", self.customFont, functCommand=None, cornerRad=2)
        self.hvSwitchOff = myButton(self,'#f8333c','#c50711', '#0d0b1e', 80, 30, "Off", self.customFont, functCommand=None, cornerRad=2)
        
        self.peltierSwitchOn = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 80, 30, "On", self.customFont, functCommand=None, cornerRad=2)
        self.peltierSwitchOff = myButton(self,'#f8333c','#c50711', '#0d0b1e', 80, 30, "Off", self.customFont, functCommand=None, cornerRad=2)
        
        self.chillerSwitchOn = myButton(self,'#61d095','#2f9d62', '#0d0b1e', 80, 30, "On", self.customFont, functCommand=None, cornerRad=2)
        self.chillerSwitchOff = myButton(self,'#f8333c','#c50711', '#0d0b1e', 80, 30, "Off", self.customFont, functCommand=None, cornerRad=2)

        self.lvSwitchOn.grid(row=1, column=0, sticky='nw', padx=10)
        self.lvSwitchOff.grid(row=1, column=0, sticky='ne', padx=10)
        self.hvSwitchOn.grid(row=4, column=0, sticky='nw', padx=10)
        self.hvSwitchOff.grid(row=4, column=0, sticky='ne', padx=10)
        self.peltierSwitchOn.grid(row=7, column=0, sticky='nw', padx=10)
        self.peltierSwitchOff.grid(row=7, column=0, sticky='ne', padx=10)
        self.chillerSwitchOn.grid(row=10, column=0, sticky='nw', padx=10)
        self.chillerSwitchOff.grid(row=10, column=0, sticky='ne', padx=10)
 
        #self.LV_switch.grid(row=1, column=0,sticky='nw',padx=5)
        #self.HV_switch.grid(row=4, column=0,sticky='nw',padx=5)
        #self.Peltier_switch.grid(row=7, column=0, sticky='nw', padx=5)
        #self.Chiller_switch.grid(row=10, column=0, sticky='nw', padx=5)

        self.lvDivider = myLabel(self, "#f5efed", 100, 20, "|", ctk.CTkFont("Roboto",30))
        self.hvDivider = myLabel(self, "#f5efed", 100, 20, "|", ctk.CTkFont("Roboto",30))
        self.peltierDivider = myLabel(self, "#f5efed", 100, 20, "|", ctk.CTkFont("Roboto",30))
        self.chillerDivider = myLabel(self, "#f5efed", 100, 20, "|", ctk.CTkFont("Roboto",30))

        self.lvDivider.grid(row=1, column=1, sticky='nw')
        self.hvDivider.grid(row=4, column=1, sticky='nw')
        self.peltierDivider.grid(row=7, column=1, sticky='nw')
        self.chillerDivider.grid(row=10, column=1, sticky='nw')

        self.lvOptionsVar = ctk.StringVar()
        self.hvOptionsVar = ctk.StringVar()
        self.peltierOptionsVar = ctk.StringVar()
        self.chillerOptionsVar = ctk.StringVar()

        self.lvOptions = ctk.CTkOptionMenu(self, values=["2.1 V, 5.88 A", "2.1 V, 6.60 A"], variable=self.lvOptionsVar, font=self.customFont, width=150)
        self.hvOptions = ctk.CTkComboBox(self, values=["80", "120"], variable=self.hvOptionsVar, font=self.customFont, width=100)
        self.peltierOptions = ctk.CTkEntry(self, textvariable=self.peltierOptionsVar, font=self.customFont, width=60)
        self.chillerOptions = ctk.CTkEntry(self, textvariable=self.chillerOptionsVar, font=self.customFont, width=60)

        self.lvOptions.grid(row=1, column=2, sticky='ne')
        self.hvOptions.grid(row=4, column=2, sticky='ne')
        self.peltierOptions.grid(row=7, column=2, sticky='ne')
        self.chillerOptions.grid(row=10, column=2, sticky='ne')

        self.hvText = myLabel(self, '#f5efed', 50,20, "V", self.customFont)
        self.peltierText = myLabel(self, "#f5efed", 50,20, "V", self.customFont)
        self.chillerText = myLabel(self, "#f5efed", 50,20,"°C", self.customFont)

        self.hvText.grid(row=4,column=3, sticky='nw')
        self.peltierText.grid(row=7,column=3, sticky='nw')
        self.chillerText.grid(row=10,column=3, sticky='nw')


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

class DCS_Selection_Bar(ctk.CTkFrame):
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
