import numpy as np
from scipy.optimize import leastsq
import time

def residuos(p, y, x):
	A, k, theta = p
	return y - (A*(np.sin(k*x + theta)))

class Integrador:
	def __init__ (self, FrecSampleo = 30):
		self.SalSave = [0, 0]
		self.Entradas = [0, 0]
		self.T = 1/FrecSampleo
		self.coef = [self.T/3, 4*self.T/3, self.T/3]
		self.anterior = 0

	def Integrar(self, senalIn):
		self.Entradas.pop(0)
		self.Entradas.append(senalIn)
		auxiliar = self.anterior + self.T*self.Entradas[1]/2 + self.T*self.Entradas[0]/2
		anterior = auxiliar
		#self.SalSave.pop(0)
		#self.SalSave.append(auxiliar)
		return auxiliar

class Desfasador:
	def __init__(self):
		self.In1 = Integrador()
		self.In2 = Integrador()

	def Desfasar(self, senalIN):
		primerPaso = self.In1.Integrar(senalIN)
		segundoPaso = self.In1.Integrar(primerPaso)
		division = senalIN/segundoPaso
		raiz = np.sqrt(abs(division))
		desfasado = (-1)*raiz * primerPaso
		amplitud = np.sqrt((senalIN**2) + (desfasado**2))
		return [desfasado, amplitud, raiz]

class Digital:
	def __init__(self):
		self.Ultimo = 0;
		self.Ultimos_valores = []
		self.Encontrado = 2
		self.Indices = -1
		self.ceros = []
		self.Inicia = True
		self.Contando = 0

	def Desfasar(self, senalIn):
		
		if self.Encontrado != 0:
			if (senalIn > 0 and self.Ultimo < 0):
				self.Encontrado = self.Encontrado - 1
				self.ceros.append(self.Indices)
			if (senalIn < 0 and self.Ultimo > 0): 		
				self.Encontrado = self.Encontrado - 1
				self.ceros.append(self.Indices)
			self.Ultimo = senalIn
			self.Indices = self.Indices + 1
			return 0, senalIn

		else:
			if self.Inicia:
				Largo = self.ceros[1] - self.ceros[0]
				if self.Contando < (Largo//2):
					self.Contando = self.Contando  + 1
					self.Ultimos_valores.append(senalIn)
				else:
					self.Inicia = False
				return 0, senalIn
			else: 	
				self.Ultimos_valores.append(senalIn)
				Auxiliar = self.Ultimos_valores[0]
				self.Ultimos_valores.pop(0)
				return Auxiliar, senalIn 

class DigitalPro:
	def __init__(self):
		self.Ultimo = 0;
		self.Ultimos_valores = []
		self.Lista_maximo = []
		self.to = time.time()
		self.Tiempo = []
		self.Encontrado = 2
		self.Indices = -1
		self.ceros = []
		self.Inicia = True
		self.Contando = 0
		self.Maximo = 0
		self.Largo = 0

	def Desfasar(self, senalIn):
		
		if self.Encontrado != 0: 					#Encontrado inicializa con 2
			if (senalIn > 0 and self.Ultimo < 0):	# Ultimo es el ultimo valor que salio
				self.Encontrado = self.Encontrado - 1
				self.ceros.append(self.Indices)
			if (senalIn < 0 and self.Ultimo > 0): 
				self.Encontrado = self.Encontrado - 1
				self.ceros.append(self.Indices)
			self.Ultimo = senalIn
			self.Indices = self.Indices + 1
			return 0, senalIn

		else:
			if self.Inicia:
				self.Largo = self.ceros[1] - self.ceros[0]
				if self.Contando < (self.Largo//2):
					self.Contando = self.Contando  + 1
					self.Ultimos_valores.append(senalIn)
					self.Lista_maximo.append(senalIn)
				else:
					self.Inicia = False
				return 0, senalIn
			else:
				self.Ultimos_valores.append(senalIn)
				self.Lista_maximo.append(senalIn)
				
				self.Maximo = 0
				
				for numero in self.Lista_maximo:
					if abs(numero) > self.Maximo:
						self.Maximo = abs(numero)
				
				Auxiliar = self.Ultimos_valores[0]/self.Maximo
				Auxiliar2 = senalIn/self.Maximo
				self.Ultimos_valores.pop(0)
				if self.Contando < (self.Largo+2):
					self.Contando = self.Contando  + 1
				else:
					self.Lista_maximo.pop(0)
				return Auxiliar, Auxiliar2 
