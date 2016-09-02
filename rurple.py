from mapa import Mapa
from robot import Robot
def cargar_mapa(nombre):
	name= open(nombre, "r")
	lista = []
	robot = Robot(0,0)
	for linea in name:
		lista.append(list(linea))
	return lista	

for numero in linea:
	if numero==0:
		print(" " 0="")

Mapa1=("mapa.txt")
Mapa2=("mapa1.txt")

print("ingrese el numero del mapa deseado:\n1. mapa1\n 2.mapa2")	
opc=int(input("ingrese el numero: "))
if opc==1:
	print(cargar_mapa(Mapa1))

	

