import time
import gpib
import matplotlib.pyplot as plt
import numpy as np
import time

class HP:

	def __init__ (self, addres):
		self.equipo = gpib.dev(0,addres)
		self.addres = addres
	def leer (self):
		aa = gpib.read(self.equipo,13)
		return float(aa)
	def mandar (self,mensaje):
		bb = gpib.write(self.equipo,mensaje)
	def rango(self, ra):
		cc = gpib.write(self.equipo,"R"+ra)
	def Set(self):
		self.mandar(b"T2")
		self.mandar(b"F1R1Z1N3")
		print("Seteado del equipo "+ str(self.addres)+" Termiando")

#Equipo1 = HP(5)
#Equipo2 = HP(3)
#Equipo2.Set()
#Equipo1.Set()

#to = time.time()
#tiempo = []
#puntos1 = []
#puntos2 = []

#N = 50

#for i in range(0,N):
	#tiempo.append(time.time()-to)
	#puntos1.append(Equipo1.leer())
	#puntos2.append(Equipo2.leer())

#print(tiempo[-1])


#archivo = open("E1yE2.txt", "w")

#for i in range(0,N):
	#archivo.write(str(tiempo[i])+"\t"+str(puntos1[i])+"\n")
	#archivo.write(str(tiempo[i])+"\t"+str(puntos2[i])+"\n")

#plt.plot(tiempo, puntos1, "b")
#plt.plot(tiempo, puntos2, "r")
#plt.show()


#Equipo3 = HP(2)
#Equipo3.mandar(b"*IDN?")


