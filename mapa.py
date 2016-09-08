class Mapa(object):
 
	def __init__(self, altura, ancho, fichas, robot):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

			
lista_mapa=[]
mapa="p"
mapa=Mapa(len(lista_mapa[0],lista_mapa))
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
				if x == self.robot.x and y == self.robot.y:
					resultado += self.robot.dibujar()
				if self.contar_monedas_en(x,y):
					pass
				else:
					resultado += " "
					resultado += "\n"
			return resultado	

	def contar_fichas(self,x,y):
		conteo = 0
		for moneda in self.moneda:
				if ficha.y == y and ficha.x == x:
					conteo += 1
		return conteo
	
	def asignar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, moneda):
		self.monedas.append(moneda)

	def remover_moneda_en(self, x, y):
		indice_coincidencia = -1
		for indice in range(len(self.monedas)):
			moneda = self.monedas[indice]
			if moneda.x == x and moneda.y == y:
				indice_coincidencia = indice
				break

		if indice_coincidencia >= 0:

			self.monedas.pop(indice_coincidencia)    