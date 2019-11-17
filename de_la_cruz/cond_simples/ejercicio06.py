import os
#declarar variables
distancia,velocidad=0.0,0.0

#INPUT
distancia=float(os.sys.argv[1])
velocidad=float(os.sys.argv[2])

#PROCESSING
tiempo=(distancia/velocidad)

#OUPUT
print(" ############################################# ")
print(" # CONCURSO DE CARRERA DE AUTOS # ")
print("distancia recorrida de: ", distancia)
print("velocidad: ", velocidad)

#VERIFICADOR
Tiempo=(tiempo<2)

#condicional simple
#si el chofer llega a la meta en menos de 2 horas a ganado el concurso
if(Tiempo==True):
    print("Ganaste el concurso")

#fin_if
