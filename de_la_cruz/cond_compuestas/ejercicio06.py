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

#condicional multiple
#si la carrera lo haces en 50min ganas una moto lineal
#si la carrera lo haces en 40min ganas 150 soles
#si la carrera lo haces en menos de 40min ganas una moto lineal

if(tiempo==50):
    print("usted ha ganado una moto lineal")
if(tiempo==40):
    print("usted a ganado 150 soles")
if(tiempo<40):
    print("usted no ha ganadado nada")

#fin_if
