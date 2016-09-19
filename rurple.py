from mapa import Mapa
from robot import Robot
import time

def cargar_mapa(nombre):
	name= open(nombre, "r")
	lista=[]
	for i in Mapa:
		lista.append(list(i.strip()))
	Mapa.close()	
	return lista
def cargar_instrucciones(nombre):
	name=open(nombre,"r")
	instrucciones=[]
	for i in instrucciones:
		instrucciones.append(i.strip())

nombre_mapa=input("ingrese el nobre del archivo: ")
nombre_instrucciones=input("ingrese las instrucciones: ")
lista_mapa=cargar_mapa(nombre_mapa)
nombre_instrucciones=cargar_instrucciones(nombre_instrucciones)
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
print(objeto_mapa.didujar())


for x in lista_intrucciones:
	if x =="rotar":
		objeto_robot.rotar()

	if x=="mover":
		objeto_robot.mover()

	if x=="recojer":
		objeto_robot.recojer()


print("\n")
print("monedas restantes: " + objeto_mapa.monedas_en_mapa())
print("monedas obtenidas: " + objeto_robot.monedas)
print(objeto_mapa.dibujar())
print("\n")


print(objeto_mapa.dibujar())
time.sleep(0.4)


