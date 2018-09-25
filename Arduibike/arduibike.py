#!/usr/bin/python3
# -*- coding: utf-8 -*-

#======================
# Imports
#======================
import tkinter as tk
from tkinter import ttk
import random


#======================
# Class
#======================

# Widget DigitalMeter
class DigitalMeter :
    
    # Constructeur
    def __init__(self, parent_widget,**config_args):
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

        # construction du widget
        self.frame = tk.Frame(parent_widget,width=config['width'],height=config['height'],bd=2,relief=tk.RIDGE)
        self.frame.pack(padx=50 , pady=10)
        # Label
        self.lbl = tk.Label(self.frame, width=10, font=("Arial",20),text=config['title'], fg = '#222')
        self.lbl.grid(column=0, row=0, sticky = 'E')
        # Valeur
        self.lbl_num = tk.Label(self.frame, font=("Arial",40,"bold"))
        self.set(config['num_value'])
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


#==============================
# Events Handlers (callback)
#==============================

# Quitte l'application et ferme la fenetre
def _quit():
    win.destroy()

# Copie/Affiche les mesures courante dans le digitmeter mémo
def _memo_mesures():
    digit_tension_memo.set( digit_tension.get() )
    digit_intensity_memo.set( digit_intensity.get() )
    digit_power_memo.set(digit_power.get())

# Remet tout les digitmeters à zero
def _reset_mesures():
    digit_tension_memo.set(0)
    digit_intensity_memo.set(0)
    digit_power_memo.set(0)
    digit_tension.set(0)
    digit_intensity.set(0)
    digit_power.set(0)

# Start / Stop les mesures
def _start_mesures():
    global _do_mesures
    _do_mesures = 0 if _do_mesures else 1
    txt_btn =  'STOP ' if _do_mesures else 'START'
    btn_start.configure(text = txt_btn)
    if(_do_mesures):
        win.after(1000,_update_mesures)

# Simulation de l'acquisition avec RANDOM
# @TODO implémenter Arduino
def _acquisition_mesures():
    mesure = {'tension':0, 'intensity':0, 'power':0}
    mesure['tension'] = random.uniform(0.5, 5)
    mesure['intensity'] = random.uniform(0.2, 2)
    mesure['power'] = mesure['tension'] * mesure['intensity']
    return mesure

# Mise à jour des messures toutes les secondes
def _update_mesures():
    global _do_mesures
    mesure = _acquisition_mesures()
    digit_tension.set(mesure['tension'])
    digit_intensity.set(mesure['intensity'])
    digit_power.set(mesure['power'])
    if(_do_mesures):
        win.after(1000,_update_mesures)


# Variable (flag) pour savoir si on doit faire l'acquisition des mesures
# 0 = off
# 1 = on  _update_mesures() est appelé toutes les secondes
_do_mesures = 0



#======================
# Interface
#======================

# Pour positionner tout les éléments on utilise le gestionnaires de positionnement "grid" (geometry managers) 
# @see : http://tkinter.fdex.eu/doc/gp.html
# @see : http://effbot.org/tkinterbook/grid.htm
# Note la methode .grid() fait référence à la grille contenu dans le widget Parent
# donc ici la fenêtre principlale "win"
#
#  ---------------------------
# | col=0 row=0 | col=1 row=0 |
#  ---------------------------
# | col=0 row=1 columnspan=2  |
#  ---------------------------

# Fenetre principale
win = tk.Tk()

# Ajout du titre
win.title("Arduino Vélo Monitoring")

# Créeation des widgets DigitalMeter pour le monitoring en continue
frame_mesure_monitor = tk.LabelFrame(win, text = 'Mesures en continu')
digit_tension = DigitalMeter(frame_mesure_monitor, title="Tension \n (en volt)", num_value = 0)
digit_intensity = DigitalMeter(frame_mesure_monitor, title="Intensité \n (en Ampère)", num_value = 0)
digit_power = DigitalMeter(frame_mesure_monitor, title="Puissance \n (en W)", num_value = 0)
frame_mesure_monitor.grid(column=0, row=0, sticky = 'W', padx=8, pady=8)

# Créeation des widgets DigitalMeter pour la mémorisation des mesures
frame_mesure_memo = tk.LabelFrame(win, text = 'Mesures mémorisées')
digit_tension_memo = DigitalMeter(frame_mesure_memo, title="Tension \n (en volt)")
digit_intensity_memo = DigitalMeter(frame_mesure_memo, title="Intensité \n (en Ampère)")
digit_power_memo = DigitalMeter(frame_mesure_memo, title="Puissance \n (en W)", num_value = 0)
frame_mesure_memo.grid(column=1, row=0, sticky = 'W', padx=8, pady=8)

# Créeation des bouttons d'actions et 
frame_actions = tk.LabelFrame(win, text = 'Actions')
btn_start = tk.Button(frame_actions, text = 'START', command=_start_mesures, width=10)
btn_start.grid(column=0, row=0, sticky = 'W', padx=8, pady=8)
btn_memo = tk.Button(frame_actions, text = 'Mémoriser', command=_memo_mesures)
btn_memo.grid(column=1, row=0, sticky = 'W', padx=8, pady=8)
btn_reset = tk.Button(frame_actions, text = 'Reset', command=_reset_mesures)
btn_reset.grid(column=2, row=0, sticky = 'W', padx=8, pady=8)
btn_quit = tk.Button(frame_actions, text = 'Quitter', command=_quit)
btn_quit.grid(column=3, row=0, sticky = 'W', padx=8, pady=8)
frame_actions.grid(row=1, columnspan=2, padx=8, pady=8, sticky = 'WE')


#======================
# Start GUI
#======================
win.mainloop()
