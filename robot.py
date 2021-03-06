class Robot(object):
	def __init__(self, posicion_x, posicion_y):
		self.x	= x
		self.y = y
		self.rotacion = 0
		self.mapa = None
		self.fichas = 0

	def dibujar(self):
		if self.rotacion == 0:
			return "^"
		elif self.rotacion == 1:
			return ">"
		elif self.rotacion == 2:
			return "v"
		return "<"

	def colocar_en_mapa(self,mapa):
		self.mapa = mapa

	def mover(self):
		if self.rotacion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.rotacion == 1:
			self.x += 1
			if self.x > 79:
				self.x = 79
		if self.rotacion == 2:
			self.y += 1
			if self.y > 49:
				self.y = 49
		else:
			self.x -= 1
			if self.x < 0:
				self.x = 0


		if self.x >= self.mapa.ancho:
			self.x = self.mapa.ancho - 1

		if self.y < 0:
			self.y = 0

		if self.y >= self.mapa.altura:
			self.y = self.mapa.altura - 1

	def rotar(self):
		if self.direccion == 0:
			self.direccion = 1
		elif self.direccion == 1:
			self.direccion = 2
		elif self.direccion == 2:
			self.direccion = 3
		else:
			self.direccion = 0	
	def asingar_mapa(self, mapa):
		self.mapa = mapa

	def recoger(self):
		if self.mapa.contar_monedas_en(self.x, self.y) > 0:
			self.monedas += 1
			self.mapa.remover_moneda_en(x, y)		

            