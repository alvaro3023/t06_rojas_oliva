import os
#declarar variables
distancia,velocidad=0.0,0.0

#INPUT
distancia=float(os.sys.argv[1])
velocidad=float(os.sys.argv[2])

#PROCESSING
tiempo=int(distancia/velocidad)

#OUPUT
print(" ############################################# ")
print(" # CONCURSO DE CARRERA DE AUTOS # ")
print("distancia recorrida de: ", distancia)
print("velocidad: ", velocidad)

#VERIFICADOR
Tiempo=(tiempo<2)

#condicional doble
#si el chofer llega a la meta en menos de 2 horas a ganado el concurso
#si el chofer llega pasa las 2 horas habra perdido

if(Tiempo==True):
    print("Ganaste el concurso")
else:
    print("Perdiste")
#fin_if
