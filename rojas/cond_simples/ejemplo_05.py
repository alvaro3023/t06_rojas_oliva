import os
#DENSIDAD DE UN LIQUIDO X
#DECLARAR VARIABLES
masa,velocidad,volumen=0.0,0,0.0

#INPUT
masa=float(os.sys.argv[1])
velocidad=int(os.sys.argv[2])
volumen=float(os.sys.argv[3])

#PROCESSING
densidad =(masa/velocidad)*volumen

#VERIFICADOR
densidad_verificado =(densidad <= 100)

#OUTPUT
print("EL valor de la masa es: " + str(masa))
print("El valor de la velocidad es: " + str(velocidad))
print("El valor de la densidad es: " + str(densidad))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _  _ _ _")

#CONDICIONAL SIMPLE
#SI LA DENSIDAD ES MENOR O IGUAL A 100 ENTONCES LA DENSIDAD ES OPTIMA
if (densidad_verificado== True):
    print("LA DENSIDAD ES OPTIMA")

#fin_if
