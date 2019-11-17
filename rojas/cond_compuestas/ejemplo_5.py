import os
#DENSIDAD DE UN LIQUIDO X
#DECLARAR VARIABLES
masa,velocidad,volumen=0.0,0,0.0

#INPUT
masa=float(os.sys.argv[1])
velocidad=int(os.sys.argv[2])
volumen=float(os.sys.argv[3])

#PROCESSING
densidad =(round(masa/velocidad*volumen,2))

#VERIFICADOR
densidad_verificado =(densidad >=1000)

#OUTPUT
print("EL valor de la masa es: " + str(masa))
print("El valor de la velocidad es: " + str(velocidad))
print("El valor de la densidad es: " + str(densidad))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _  _ _ _")

#CONDICIONAL SIMPLE
#SI LA DENSIDAD ES MAYOR O IGUAL A 1000 ENTONCES LA DENSIDAD ES OPTIMA
if (densidad_verificado== True):
    print("LA DENSIDAD ES OPTIMA")

if (densidad<300):
    print("LA DENSIDAD NO ES OPTIMA")

if (densidad>300 and densidad<1000):
    print("LA DENSIDAD SE MANTIENE")
#fin _if
