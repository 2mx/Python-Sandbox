import sys
import re
import serial

# Création d'une connection serie
# Pour la gestion des exceptions 
# @see: http://apprendre-python.com/page-apprendre-exceptions-except-python-cours-debutant
try :
    conn_serial = serial.Serial(port="COM4", baudrate=9600, timeout=1, writeTimeout=1)
except serial.serialutil.SerialException as errorException :
   print(  "Erreur de connection avec le port série : " , errorException )
   sys.exit()

while True:
    # Lecture
    data = conn_serial.readline()

    # Extraction et validation des données avec une expression régulière
    # Les données doivent être au format : 8.25;1.41 (il peut y avoir des caractères avant et/ou aprés)
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
    