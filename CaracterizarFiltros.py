from scipy import signal
import matplotlib.pyplot as plt
import time
import numpy as np
from Equipos import Multimetro
from Clases import Filtro
#--------------------------------------------

## Caracterizar Filtros

NombreArchivo = "CarO5FC01.txt"

Filtro = Filtro.Filtro(5, 0.1)
Equipo1 = Multimetro.HP(5)
Equipo1.Set()

archivo = open(NombreArchivo, "w")
archivo.close()

to = time.time()

while(True):
	time.sleep(0.001)
	archivo = open(NombreArchivo, "a")
	senalIN = Equipo1.leer()
	archivo.write(str(time.time()-to)+"\t"+str(senalIN)+"\t"+str(Filtro.filtrar(senalIN))+"\n")
	archivo.close()
