from scipy import signal
import matplotlib.pyplot as plt
import time
import numpy as np
from Equipos import Multimetro
from Clases import Filtro, Post
#--------------------------------------------

## Prueba con referencia interna

NombreArchivo = "Rueda/F12.95Fc0.1"	# O es Orden, FC es Frecuencia de Corte, D es Desfasaje de frecuencia
NombreArchivoFiltro = NombreArchivo + "_Datos" + ".txt" 
NombreArchivo = NombreArchivo + ".txt"
Pos = Post.PostProcesado()
prod = Post.Producto(12.95)
Filtro1 = Filtro.Filtro(4, 0.1)
Filtro2 = Filtro.Filtro(4, 0.1)
Equipo1 = Multimetro.HP(5)
Equipo1.Set()

archivo = open(NombreArchivo, "w")
archivo.close()
archivo1 = open(NombreArchivoFiltro, "w")
archivo1.close()

to = time.time()
tau = 40
print("\nEmpezo a medir\n")
while(time.time()-to< (10*tau)):
	time.sleep(0.001)
	archivo = open(NombreArchivo, "a")
	senalIN = Equipo1.leer()
	tiempo = time.time()-to
	auxiliar = prod.do(tiempo, senalIN)
	coseno, seno = Filtro1.filtrar(auxiliar[0]), Filtro2.filtrar(auxiliar[1])
	auxiliar2 = Pos.procesar(seno, coseno)
	archivo.write(str(tiempo)+"\t"+str(auxiliar2[0])+"\t"+str(auxiliar2[1])+"\t"+str(senalIN)+"\n")
	# 				1					2						3					4		
	if time.time()-to> tau:
		archivo1 = open(NombreArchivoFiltro, "a")
		archivo1.write(str(tiempo)+"\t"+str(auxiliar2[0])+"\t"+str(auxiliar2[1])+"\t"+str(senalIN)+"\n")
		archivo1.close()
	archivo.close()

print("---------------------------\nTermino de medir\n---------------------------")
