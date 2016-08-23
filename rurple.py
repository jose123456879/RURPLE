from cargar_mapa import cargar_mapa

Mapa1=("mapa.txt")
Mapa2=("mapa1.txt")

opc=int(input("ingrese el mapa deseado:\n1. mapa1 \n2.mapa2"))
if opc==1:
	print(cargar_mapa(Mapa1))

	

