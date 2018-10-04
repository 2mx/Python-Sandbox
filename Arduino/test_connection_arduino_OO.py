import sys
import re
import serial

class ArduinoSerialUIData:
    def __init__(self, serialport = 'COM4'):
        # Création d'une connection serie
        self.serialcnx = serial.Serial(port=serialport, baudrate=9600, timeout=1, writeTimeout=1)
        
    def getmesures():
        # Lecture Arduino
        # Wait here until there is data
        while (self.serialcnx.inWaiting()==0): 
            pass #do nothing
            
        # Les données envoyées par arduino sont reçut par python au format "bytes object" : b'0.0;2.9\r\n'
        # le b indique que les données sont au format bytes object 
        # @see: https://www.geeksforgeeks.org/byte-objects-vs-string-python/
        # @see: https://www.pythoncentral.io/encoding-and-decoding-strings-in-python-3-x/
        # on utilise la methode .decode() pour convertir les données en caractères
        data = self.serialcnx.readline().decode('ascii')

        # Extraction et validation des données avec une expression régulière
        # Les données doivent être au format : 8.25;1.41 (il peut y avoir des caractères avant et/ou aprés)
        # @see: http://apprendre-python.com/page-expressions-regulieres-regular-python
        matchObj = re.match( r'.*(\d+\.\d+);(\d+\.\d+).*', data)
        if(matchObj) : 
            mesures = {'tension':0, 'intensity':0, 'power':0}
            # traitement
            mesures['tension']    = float(matchObj.group(1))
            mesures['intensity']  = float(matchObj.group(2))
            mesures['puissance']  = mesures['tension']*mesures['intensity']
            return mesures
        # problème avec le format de donné transmis
        # on relance une lecture
        else :
            self.getmesures()



class AppArduinoUI:
    def __init__(self, serialport = 'COM4'):
        self.serialport = serialport

    def run(self):
        # Création d'une connection avec Arduino
        # Pour la gestion des exceptions 
        # @see: http://apprendre-python.com/page-apprendre-exceptions-except-python-cours-debutant
        try :
            arduinodata = ArduinoSerialUIData(self.serialport)
        except serial.serialutil.SerialException as errorException :
           print(  "Erreur de connection avec le port série : " , errorException )
           sys.exit()
        while True:
            mesures = arduinodata.getmesures()
            # Affichage
            print("T = {:.2f} V | I = {:.2f} A | P = {:.2f} W".format(mesures['tension'], mesures['intensity'], mesures['puissance']) )
           
            


app = AppArduinoUI('COM4')
app.run()