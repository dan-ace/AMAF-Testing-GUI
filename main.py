import tkinter
import customtkinter as ctk # <- import the CustomTkinter module                                                                                                                
from tkinter import filedialog
from classes import *
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

        self.yarrFrame = Yarr_Frame(parent=self, app=self)
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
    
if __name__=="__main__":
    app = App()
    app.mainloop()
