import os
#SUPERFICIE DE UN CILINDRO
#DECLARAR VARIABLES
pi,radio_base,altura_cilindro=0.0,0,0

#INPUT
pi=float(os.sys.argv[1])
radio_base=int(os.sys.argv[2])
altura_cilindro=int(os.sys.argv[3])

#PROCESSING
Superficie_cilindro=(round(2*pi*radio_base*altura_cilindro,2))

#VERIFICADOR
Superficie_cilindro_verificado =(Superficie_cilindro < 100)

#OUTPUT
print("El pi es: " + str(pi))
print("El radio es: " + str(radio_base))
print("La altura es: " + str(altura_cilindro))
print("La superficie de un cilindro es: " + str(Superficie_cilindro))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _  _ _ _")

#CONDICION SIMPLE
#SI LA SUPERFICIE DEL CILINDRO ES MENOR DE 100 ES CORRECTO
if (Superficie_cilindro_verificado== True):
    print("EL AREA DE LA SUPERFICIE DEL CILINDRO ES CORRECTO")

if (Superficie_cilindro>100):
    print("EL AREA DE LA SUPERFICIE ES INCORRECTA")
if (Superficie_cilindro == 99 ):
    print("EL AREA DE LA SUPERFICIE ESTA ENTRE LOS RANGOS ACEPTABLE")
#fin_if
