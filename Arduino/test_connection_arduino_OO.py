import sys
import re
import serial



class ArduinoSerialUIData:
    """ 
    Class pour se connecter à Arduino via le port serie
    et lire les données envoyées : tension et intensité via getmesures()
    """

    def __init__(self, serialport = 'COM2'):
        # Création d'une connection serie
        self.serialcnx = serial.Serial(port=serialport, baudrate=9600, timeout=1, writeTimeout=1)
        
    def getmesures():
        """ 
        Lis les données arduino envoyées et retourne un tableau de mesures tension, intensité et puissance
        mesures = {'tension':0, 'intensity':0, 'power':0}
        """

        # Lecture Arduino
        # On attend qu'il y ait des données (in_waiting = Get the number of bytes in the input buffer)
        while (self.serialcnx.in_waiting()==0): 
            pass #do nothing
            
        # Les données envoyées par arduino transit sous un format binaire
        # et sont reçut tel quel par python
        # c'est ce qu'indique le b pour "bytes object" : b'0.0;2.9\r\n'
        # @see: https://www.geeksforgeeks.org/byte-objects-vs-string-python/
        # @see: https://www.pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
        # on utilise la methode .decode() pour convertir les données binaire en caractères
        data = self.serialcnx.readline().decode('ascii')

        # Extraction et validation des données avec une expression régulière
        # Les données doivent être au format : 12.25;1.412
        # @see: http://apprendre-python.com/page-expressions-regulieres-regular-python
        # On pourrait se passer d'une expression régulère en utilisant data.split(';')
        # mais si pour une raison x ou y les données sont corompus on risque le plantage
        matchObj = re.match( r'(\d+\.\d+);(\d+\.\d+)', data)
        if(matchObj) : 
            mesures = {'tension':0, 'intensity':0, 'power':0}
            # traitement
            mesures['tension']    = float(matchObj.group(1))
            mesures['intensity']  = float(matchObj.group(2))
            mesures['power']  = mesures['tension']*mesures['intensity']
            return mesures
        # problème avec le format de donné transmis
        # on relance une lecture
        else :
            self.getmesures()



class AppArduinoUI:
    def __init__(self, serialport = 'COM2'):
        self.serialport = serialport

    def run(self):
        # Création d'une connection avec Arduino
        # Pour la gestion des exceptions 
        # @see: http://apprendre-python.com/page-apprendre-exceptions-except-python-cours-debutant
        try :
            arduinodata = ArduinoSerialUIData(self.serialport)
        except Exception  as excep :
           print(  "Erreur de connection avec le port série : " , excep )
           print("Exception de type ", excep.__class__)
           sys.exit()
        while True:
            mesures = arduinodata.getmesures()
            # Affichage
            print("T = {:.2f} V | I = {:.2f} A | P = {:.2f} W".format(mesures['tension'], mesures['intensity'], mesures['power']) )
           

# Pour afficher la documentation           
#print (ArduinoSerialUIData.__doc__)
#help (ArduinoSerialUIData)

app = AppArduinoUI('COM4')
app.run()