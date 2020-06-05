"""
RETO 1:
Implementar el juego de las cerillas: Se parte de un número inicial de cerillas. 
Hay 2 jugadores que se van turnando. Inicialmente no saben el número de cerillas que hay. 
Cada jugador toma 1, 2 o 3 cerillas en su turno. 
Pierde el jugador que se queda con la última cerilla.
"""
import random

#cerillas = random.randrange(101)
#cerillas = random.randint(100)
cerillas = 10
print(cerillas)

turno = 0

while cerillas > 0:
	n = int(input("Jugador %d es tu turno: "%(turno+1)))
	if n<1 or n>3:
		print("Jugador %d debes introducir un valor entre 1 y 3"%(turno+1))
	else:
		if n>=cerillas:
			print("Jugador %d has perdido. Quedaban %d cerillas"%(turno +1,cerillas))
			cerillas = 0
		else:
			cerillas -= n
			print("Jugador %d has retirado %d cerillas."%(turno+1, n))
			turno += 1
			turno = turno % 2
print("Fin del juego")