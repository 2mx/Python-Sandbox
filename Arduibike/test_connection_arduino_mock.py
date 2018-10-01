#!/usr/bin/python
import re

# Lecture
datas = ['5.231;1.47', 'p6.324;1.481\n', '2.23;', '15.23;1.47154', 'pppptt2.23;2.2jhjhj', 'p;1.47\n']


for data in datas : 
    # Extraction et validation des données avec une expression régulière
    # Les données doivent être au format : 8.25;1.41
    # @see: http://apprendre-python.com/page-expressions-regulieres-regular-python
    matchObj = re.match( r'.*(\d+\.\d+);(\d+\.\d+).*', data)
    if(matchObj) : 
    	# traitement
    	tension   = float(matchObj.group(1))
    	intensity = float(matchObj.group(2))
    	puissance = tension*intensity

    	# Affichage
    	print("Tension   = {:.2f} V".format(tension) )
    	print("Intensité = {:.2f} A".format(intensity) )
    	print("Puissance = {:.2f} W".format(puissance) )
    else :
    	print(" >>>>>>>>>>>>> Erreur de lecture")
    print(" -----------------------")
    