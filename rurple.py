from mapa import Mapa
from robot import Robot
def cargar_mapa(nombre):
	name= open(nombre, "r")
	lista = []
	robot = Robot(0,0)
	for linea in name:
		lista.append(list(linea))
	return lista	
def cargar_instrucciones(nombre):
	archivo=open(nombre,"r")
	lista_intrucciones=[]
	

Mapa1=("mapa.txt")
Mapa2=("mapa1.txt")

print("ingrese el numero del mapa deseado:\n1. mapa1\n2. imapa2")	
opc=int(input("ingrese el numero: "))
if opc==1:
	print(cargar_mapa(Mapa1))



