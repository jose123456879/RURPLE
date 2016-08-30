class Robot(object):
	def __init__(self,x, y):
		self.posicion_x	= 0
		self.pocicion_y = 0
		self.rotacion = 1
		self.pick = False
		self.mapa = mapa
		self.fichas = 0
	
	def Rotar(self):
		self.rotacion += 1
		if self.rotacion == 5:
			self.rotacion = 1
	def recoger_moneda(self):
		if Hay_ficha(self.x, self.y):
			mapa.quitar_ficha(self.x,self.y)
			self.fichas += 1
			