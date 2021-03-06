#!/usr/bin/python3
# -*- coding: utf-8 -*-

#======================
# Imports
#======================
import tkinter as tk
from tkinter import ttk


#======================
# Widget DigitalMeter - Class dérivé (hérité) de tk.Frame
#======================

class DigitalMeter(tk.Frame) :
    
    # Constructeur
    def __init__(self, master,**config_args):
        # Constructeur du widget parent
        super().__init__(master)

        # config par defaut
        config = {
            'title' : '',
            'num_value' : 0.00,
            'width' :  200,
            'height' : 200
        }
        # fusionne avec la config passée en argument
        config.update(config_args)

        self.value = 0.00

        #====
        # Construction du widget
        #====

        # Frame
        self.config(width=config['width'],height=config['height'],bd=2,relief=tk.RIDGE)
        self.pack(padx=50 , pady=10);
        # Label
        self.lbl = tk.Label(self, width=10, font=("Arial",20),text=config['title'], fg = '#222')
        # Valeur
        self.lbl_num = ttk.Label(self, font=("Arial",40,"bold"))
        self.set(config['num_value'])
        # Layout Grid
        self.lbl.grid(column=0, row=0, sticky = 'E')
        self.lbl_num.grid(column=1, row=0, sticky = 'W', padx=8)


    # Set the digitmeter value
    # Formate et affiche la valeur
    def set(self, value):
        self.value = value
        value = "{0:.2f}".format(value)
        self.lbl_num.config(text=value)

     # Get the digitmeter value
    def get(self):
        return self.value