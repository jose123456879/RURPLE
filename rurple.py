from mapa import Mapa
from robot import Robot
import time

def cargar_mapa(nombre):
	name= open(nombre, "r")
	lista_mapa = []
	robot = Robot(0,0)
	for linea in name:
		lista.append(list(linea))
	return lista	
def cargar_instrucciones(nombre):
	archivo=open(nombre,"r")
	lista_intrucciones=[]
	for i in intrucciones:
		instrucciones.append(i.strip())

Mapa1=("mapa.txt")
Mapa2=("mapa1.txt")

print("ingrese el numero del mapa deseado:\n1. mapa1\n2. imapa2")	
opc=int(input("ingrese el numero: "))
if opc==1:
	print(cargar_mapa(Mapa1))
	print(cargar_instrucciones)

objeto_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 

for x in range(len(lista_mapa)):
	for y in range(len(lista_mapa[0])):
		if lista_mapa[x][y] == "*":		
			objeto_robot = Robot(y ,x)
			objeto_robot.asignar_mapa(objeto_mapa)
			objeto_mapa.asignar_robot(objeto_robot)		
		elif int(lista_mapa[x][y]) > 0:	
			for k in range(int(lista_mapa[x][y])):
				objeto_moneda = Monedas(y , x)
				objeto_mapa.asignar_moneda(objeto_moneda)

print("\n")
print("monedas restantes: " + objeto_mapa.monedas_en_mapa())
print("monedas obtenidas: " + objeto_robot.monedas)
print(objeto_mapa.dibujar())
print("\n")



