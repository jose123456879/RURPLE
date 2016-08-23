def cargar_mapa(f):
	mapa=open(f, "r")
	lista=[]

	for linea in mapa:
		lista.append(list(linea))
	return lista
def cargar_instrucciones(i):
	intrucciones=open(i,"r")
	listA=[]
	for j in intrucciones:
		lista.append(list(j))
	return listA	