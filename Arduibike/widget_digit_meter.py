
#======================
# Imports
#======================
import tkinter
from tkinter import ttk


#======================
# Class
#======================
class DigitalMeter :
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
        self.frame = tkinter.Frame(parent_widget,width=config['width'],height=config['height'],bd=2,relief=tkinter.RIDGE)
        self.frame.pack(padx=50 , pady=10)
        # Label
        self.lbl = tkinter.Label(self.frame, width=10, font=("Arial",20),text=config['title'], fg = '#222')
        self.lbl.grid(column=0, row=0, sticky = 'E')
        # Valeur
        self.lbl_num = tkinter.Label(self.frame, font=("Arial",40,"bold"))
        self.set(config['num_value'])
        self.lbl_num.grid(column=1, row=0, sticky = 'W', padx=8)

    def set(self, value):
        """Formatage et affichage de la valeur"""
        self.value = value
        value = "{0:.2f}".format(value)
        self.lbl_num.config(text=value)

#======================
# Interface
#======================

# Fenetre principale
win = tkinter.Tk()   

# Ajouter un titre       
win.title("Test Widget DigitalMeter")  

# Créer widgets DigitalMeter pour le monitoring en continue
frame_mesure_monitor = tkinter.LabelFrame(win, text = 'Mesures en continu')
digit_tension = DigitalMeter(frame_mesure_monitor, title="Tension \n (en volt)", num_value = 5.48)
digit_intensity = DigitalMeter(frame_mesure_monitor, title="Intensité \n (en Ampère)", num_value = 1.25)
frame_mesure_monitor.grid(column=0, row=0, sticky = 'W', padx=8, pady=8)

# Créer widgets DigitalMeter pour la mémorisation des mesure
frame_mesure_memo = tkinter.LabelFrame(win, text = 'Mesures mémorisées')
digit_tension_memo = DigitalMeter(frame_mesure_memo, title="Tension \n (en volt)")
digit_intensity_memo = DigitalMeter(frame_mesure_memo, title="Intensité \n (en Ampère)")
frame_mesure_memo.grid(column=1, row=0, sticky = 'W', padx=8, pady=8)

# Mise a jour d'un widget DigitalMeter
digit_tension.set(6.48780001)

#======================
# Start GUI
#======================
win.mainloop()
