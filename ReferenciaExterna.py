
from scipy import signal
import matplotlib.pyplot as plt
import time
import numpy as np
from Equipos import Multimetro
from Clases import Filtro, Post, Desfasador
#--------------------------------------------

## Prueba con referencia externa

NombreArchivo = "PrimerPruebaReal.txt"

Pos = Post.PostProcesado()
Desfaz = Desfasador.DigitalPro()
Filtro1 = Filtro.Filtro(5, 0.05)
Filtro2 = Filtro.Filtro(5, 0.05)
Equipo1 = Multimetro.HP(5)
Equipo1.Set()
Equipo2 = Multimetro.HP(3)
Equipo2.Set()

archivo = open(NombreArchivo, "w")
archivo.close()

to = time.time()

while(True):
	time.sleep(0.001)
	archivo = open(NombreArchivo, "a")
	senalIN = Equipo1.leer()
	senalRef = Equipo2.leer()
	tiempo = time.time()-to
	movida = Desfaz.Desfasar(senalRef)	# Coseno y Seno
	auxiliar2 = Pos.doRef(senalIN, movida)
	seno, coseno = Filtro1.filtrar(auxiliar2[0]), Filtro2.filtrar(auxiliar2[1])
	auxiliar = Pos.procesar(seno, coseno)
	
	archivo.write(str(tiempo)+"\t"+str(auxiliar[0])+"\t"+str(auxiliar[1])+"\t"+str(senalIN)+"\t"+str(senalRef)+"\t"+str(movida[1])+"\t"+str(movida[0])+"\t"+str(seno)+"\t"+str(coseno)+"\n")
	# 				1					2						3					4				5					6					7				8					9
	archivo.close()
