def cargar_mapa(f):
	mapa=open(f, "r")
	lista=[]
	for linea in mapa:
		lista.append(list(linea))
	return lista

Mapa=("mapa.txt")
print(cargar_mapa(Mapa))	