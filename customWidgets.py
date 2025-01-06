import tkinter
import customtkinter as ctk # <- import the CustomTkinter module                                                                                                                
from tkinter import filedialog 
from statistics import mean
import numpy as np
import os
import os.path
import subprocess
from datetime import datetime
from functools import reduce
import time

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
    def __init__(self, parent, color, width, height, varText, font, fg_color=None):

        self.parent=parent
        self.varText=varText
        self.color=color
        self.width=width
        self.height=height
        self.font=font
        self.fg_color=fg_color
        if not self.fg_color:
            self.label = ctk.CTkLabel(parent,
                                  text=self.varText,
                                  text_color=self.color,
                                  width=self.width,
                                  height=self.height,
                                  font=self.font)
        else:
            self.label = ctk.CTkLabel(parent,
                                  text=self.varText,
                                  text_color=self.color,
                                  width=self.width,
                                  height=self.height,
                                  font=self.font,
                                  fg_color=self.fg_color)


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