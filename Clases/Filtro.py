from scipy import signal
import time
import numpy as np

class Filtro:
	def __init__ (self, OrdenFiltro, FrecCorte, FrecSampleo = 30):
		self.b, self.a = signal.butter(OrdenFiltro, 2*FrecCorte/FrecSampleo, 'low', analog = False)
		self.NumElementos = len(self.b)
		self.SenalFiltrada = [0 for i in range(self.NumElementos)]
		self.SenalSinFiltrar = [0 for i in range(self.NumElementos)]

	def filtrar(self, senalIn):
		self.SenalSinFiltrar.pop(0)
		self.SenalFiltrada.pop(0)
		auxiliar = self.b[0]*senalIn
		for i in range(1,self.NumElementos):
			auxiliar = auxiliar - self.a[i]*self.SenalFiltrada[self.NumElementos-1-i] + self.b[i]*self.SenalSinFiltrar[self.NumElementos-1-i]
		self.SenalSinFiltrar.append(senalIn)
		self.SenalFiltrada.append(auxiliar)
		return auxiliar

	def analizador(self, nombre, tiempoStart):
		resultados = []
		archivo = open(nombre, "r")
		
		# Copio mis resutlados a una lista
		for renglon in archivo:
			auxiliar = renglon.split()
			resultados.append([float(auxiliar[0]), float(auxiliar[1]), float(auxiliar[2])])
		archivo.close()
		
		# Separo los valores del filtro
		ResultadosFiltrados = [resultados[i][2] for i in range(len(resultados))]
		
		# Consigo el indice en donde esta mi tiempo elegido
		indice = 0
		while resultados[indice][0] < tiempoStart:
			indice = indice + 1

		# Corto mi lista desde donde empieza
		ResultadosFiltrados = ResultadosFiltrados[indice:]
		
		# Media de los valores
		Promedio = 0
		for numero in ResultadosFiltrados:
			Promedio = Promedio + numero
		Promedio = Promedio / len(ResultadosFiltrados)
		
		# Varianza de los valores
		Var = 0
		for numero in ResultadosFiltrados:
			Var = Var + (numero - Promedio)**2
		Var = np.sqrt(Var / len(ResultadosFiltrados))

		return [Promedio, Var]
