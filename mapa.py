class Mapa(object):
	def __init__(self, altura, ancho, fichas, robot):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

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