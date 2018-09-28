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

# Widget DigitalMeter - Class dérivé (hérité) de tk.Frame
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


#=============================
# Application ArduibikeApp
#=============================

# Ici notre application est dérivé d'un widget de type Frame 
# La fenêtre principale est injecté en argument
class ArduibikeApp(tk.Frame):
    
    # Constructeur initialise l'application
    def __init__(self, winroot=None):
        # Appel le constructeur du widget parent (via super())
        super().__init__(winroot)

        # Variable (flag) pour savoir si on doit faire l'acquisition des mesures
        # 0 = off
        # 1 = on  _update_mesures() est appelé toutes les secondes
        self._do_mesures = 0
        self.pack()
        self.create_view()


    #=============================
    # Création de l'Interface
    #=============================

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
    def create_view(self):

        # Créeation des widgets DigitalMeter pour le monitoring en continue
        frame_mesure_monitor = ttk.LabelFrame(self, text = 'Mesures en continu')
        self.digit_tension        = DigitalMeter(frame_mesure_monitor, title="Tension \n (en volt)", num_value = 0)
        self.digit_intensity      = DigitalMeter(frame_mesure_monitor, title="Intensité \n (en Ampère)", num_value = 0)
        self.digit_power          = DigitalMeter(frame_mesure_monitor, title="Puissance \n (en W)", num_value = 0)


        # Créeation des widgets DigitalMeter pour la mémorisation des mesures
        frame_mesure_memo    = ttk.LabelFrame(self, text = 'Mesures mémorisées')
        self.digit_tension_memo   = DigitalMeter(frame_mesure_memo, title="Tension \n (en volt)")
        self.digit_intensity_memo = DigitalMeter(frame_mesure_memo, title="Intensité \n (en Ampère)")
        self.digit_power_memo     = DigitalMeter(frame_mesure_memo, title="Puissance \n (en W)", num_value = 0)


        # Créeation des bouttons d'actions 
        frame_actions = ttk.LabelFrame(self, text = 'Actions')
        self.btn_start     = ttk.Button(frame_actions, text = 'START', command=self._start_mesures, width=10)
        btn_memo      = ttk.Button(frame_actions, text = 'Mémoriser', command=self._memo_mesures)
        btn_reset     = ttk.Button(frame_actions, text = 'Reset', command=self._reset_mesures)
        btn_quit      = ttk.Button(frame_actions, text = 'Quitter', command=self._quit)
        
        # Mise en page des bouttons avec 'grid' 
        self.btn_start.grid(column=0, row=0, sticky = 'W', padx=8, pady=8)
        btn_memo.grid(column=1, row=0, sticky = 'W', padx=8, pady=8)
        btn_reset.grid(column=2, row=0, sticky = 'W', padx=8, pady=8)
        btn_quit.grid(column=3, row=0, sticky = 'W', padx=8, pady=8)

        # Mise en page des frames widgets DigitalMeter et bar d'actions avec 'grid'
        frame_mesure_memo.grid(column=1, row=0, sticky = 'W', padx=8, pady=8)
        frame_mesure_monitor.grid(column=0, row=0, sticky = 'W', padx=8, pady=8)
        frame_actions.grid(row=1, columnspan=2, padx=8, pady=8, sticky = 'WE')

    #==============================
    # Events Handlers (callback)
    #==============================

    # see: https://pythonfaqfr.readthedocs.io/en/latest/prog_even_tkinter.html

    # Quitte l'application et ferme la fenetre
    def _quit(self):
        winroot.destroy()

    # Copie/Affiche les mesures courante dans le digitmeter mémo
    def _memo_mesures(self):
        self.digit_tension_memo.set( self.digit_tension.get() )
        self.digit_intensity_memo.set( self.digit_intensity.get() )
        self.digit_power_memo.set(self.digit_power.get())

    # Remet tout les digitmeters à zero
    def _reset_mesures(self):
        self.digit_tension_memo.set(0)
        self.digit_intensity_memo.set(0)
        self.digit_power_memo.set(0)
        self.digit_tension.set(0)
        self.digit_intensity.set(0)
        self.digit_power.set(0)

    # Start / Stop les mesures
    def _start_mesures(self):
        self._do_mesures = 0 if self._do_mesures else 1
        txt_btn =  'STOP ' if self._do_mesures else 'START'
        self.btn_start.configure(text = txt_btn)
        if(self._do_mesures):
            self.after(1000,self._update_mesures)

    # Simulation de l'acquisition avec RANDOM
    # @TODO implémenter Arduino
    def _acquisition_mesures(self):
        mesure = {'tension':0, 'intensity':0, 'power':0}
        mesure['tension'] = random.uniform(0.5, 5)
        mesure['intensity'] = random.uniform(0.2, 2)
        mesure['power'] = mesure['tension'] * mesure['intensity']
        return mesure

    # Mise à jour des messures toutes les secondes
    # Pour gerer le temps avec tkinter on utilise la méthode de widgets .after(delay, function, *args, **kwargs)
    # @see : https://pythonfaqfr.readthedocs.io/en/latest/prog_even_tkinter.html#gerer-le-temps
    def _update_mesures(self):
        mesure = self._acquisition_mesures()
        self.digit_tension.set(mesure['tension'])
        self.digit_intensity.set(mesure['intensity'])
        self.digit_power.set(mesure['power'])
        if(self._do_mesures):
            self.after(1000,self._update_mesures)



# le code ci-dessous sera executé seulement si appelé directement depuis ce fichier
# ce qui ne sera pas le cas avec un import
# @see https://docs.python.org/fr/3/library/__main__.html
if __name__ == "__main__":

# Start GUI

    # Fenetre principale
    winroot = tk.Tk()
    # Ajout du titre
    winroot.title("Arduino Vélo Monitoring")
    # Instance de l'application
    app = ArduibikeApp(winroot)
    # Démarre la boucle événementielle mainloop
    # @see https://pythonfaqfr.readthedocs.io/en/latest/prog_even_tkinter.html
    app.mainloop()


