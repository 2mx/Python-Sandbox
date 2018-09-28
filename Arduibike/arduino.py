# -*- coding: utf-8 -*-
import random

# Simulation de l'acquisition avec RANDOM
class SerialReadUIRandom() :

	def read(self) :
		mesures = {'tension':0, 'intensity':0, 'power':0}
		mesures['tension'] = random.uniform(0.5, 5)
		mesures['intensity'] = random.uniform(0.2, 2)
		mesures['power'] = mesures['tension'] * mesures['intensity']
		return mesures


# Acquisition U I avec serial
class SerialReadUI() :

	def read(self) :
		mesures = {'tension':0, 'intensity':0, 'power':0}
		# @todo implémenter l'aquisition des données
		return mesures