


class Mapa(object):
 
	def __init__(self, altura, ancho, fichas, robot):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

			
lista_mapa=[]
mapa==Mapa(len(lista_mapa[0],lista_mapa))
for y in range(len(lista_mapa)):
	for x in range(len(lista_mapa)):
		if lista_mapa[y][x]=="*":
			robot=Robot[x][y]
		elif lista_mapa[y][x] == "0":
			pass
		else:
			cantidad=int(lista_mapa[y][x])
			for i in range(cantidad):
				moneda=Moneda(x,y)
				mapa_agregar=moneda(moneda)

	def cargar_mapa(nombre):
		name= open(nombre, "r")
		lista = []
		robot = Robot(0,0)
		for linea in name:
			lista.append(list(linea))
		return lista	



	def dibujar(self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if ficha.x == x and ficha.y == y:
					resultado += ficha
				elif robot.x == x and robot.y == y:
					resultado += robot
				else:
					resultado += " "
			resultado += "\n"

	def contar_fichas(self,x,y):
		conteo = 0
		for y in range(self.altura):
			for x in range(self.ancho):
				if ficha.y == y and ficha.x == x:
					conteo += ficha
		return conteo

	def agregar_ficha(self,x,y):
		self.ficha.append(ficha)


	