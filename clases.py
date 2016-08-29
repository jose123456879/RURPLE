class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
	
	def asignar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, moneda):
		self.monedas.append(moneda)
lista_mapa=[....]
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

class Robot(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion="UP"
		self.mapa=None

	def MOVE(self):
		pass
	def ROTATE(self):
		pass
	def PICK(self):
		pass
	def obtener_representacion(self):
		if self.direccion=="UP":
			


class Moneda(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.mapa=None				