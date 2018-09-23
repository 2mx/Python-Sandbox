# ----------------------------------------------
# - Manipulation des chaines de caractères
# ----------------------------------------------

# avec python (3?) les chaines de caractère sont des objets. 
# on peut donc utiliser toutes les méthodes de l'objet string
# @see : https://docs.python.org/fr/3/library/stdtypes.html#string-methods
# les fonctions sont dépréciées (donc plutôt que d'utiliser la fonction format() on utilisera la methode .fotmat())


message = "Cyril programme en php"
print( message.replace("php", "python") )

x = 34.56789
# via la fonction format()
print (format(x, '0.2f'))
# ou via la methode .format()
print ("{:.2f}".format(x) )
print ("La tension est de {:.2f} volt".format(x) )
 


# ----------------------------------------------
# - Exemple acquisiton et traitement avec arduino
# ----------------------------------------------

# Acquistion mesure (<type 'string'>)
lect_arduino="5.4872;1.254"
type(lect_arduino)

# Tableau de mesures (<type 'list'>)
# split découpe une chaine de caractères selon un délimiteur (ici ;)
# et retourne un tableau
mesures = lect_arduino.split(';')
type(mesures)

# traitement
tension   = mesures[0]
intensity = mesures[1]
tension   = float(tension)
intensity = float(intensity)
puissance = int(tension*intensity)

# Affichage
# pour le formatage des données '{:.2f}'.format(value)
# voir https://pyformat.info/
print("Tension = "+ '{:.2f}'.format(tension) )
print("Intensité = "+ '{:.2f}'.format(intensity) )
print("Puissance = "+ '{:.2f}'.format(puissance) )


