import numpy as np

class PostProcesado:
	def __init__(self):
		self.Resultados = []
		self.AmplitudNueva = 0
		self.FaseNueva = 0

	def Amplitud(self, senal1, senal2):
		Auxiliar1 = senal1*senal1
		Auxiliar2 = senal2*senal2
		Auxiliar3 = np.sqrt(Auxiliar1 + Auxiliar2)
		self.AmplitudNueva =  Auxiliar3

	def fase(self, senal1, senal2):
		self.FaseNueva = np.arctan2(senal1, senal2)
	
	def procesar(self, senal1, senal2):
		self.Amplitud(senal1, senal2)
		self.fase(senal1, senal2)
		self.Resultados.append([self.AmplitudNueva, self.FaseNueva])
		return [self.AmplitudNueva, self.FaseNueva]
	def doRef(self, senalIn, senalRef):
		return [2*senalRef[0]*senalIn, 2*senalRef[1]*senalIn]

class Producto:
	def __init__(self, FrecuenciaReferencia):
		self.Frec = FrecuenciaReferencia
	def do(self,tiempo, senalIn):
		return [2*np.cos(2*np.pi*self.Frec*(tiempo)) * senalIn, 2*np.sin(2*np.pi*self.Frec*(tiempo)) * senalIn]
