import os
#VOLUMEN DE UNA ESFERA
#DECLARAR VARIABLES
pi,radio,angulo=0.0,0,0

#INPUT
pi=float(os.sys.argv[1])
radio=int(os.sys.argv[2])
angulo=int(os.sys.argv[3])

#PROCESSING
volumen =(round(4/3*pi*(radio**3)*angulo,2))

#VERIFICADOR
volumen_correcto=(volumen>=50)
#OUTPUT
print("pi es: " + str(pi))
print("El radio es: " + str(radio))
print("El angulo es:" + str(angulo))
print("El volumen de la esfera es: " + str(volumen))

#CONDICION DOBLE
# si el volumen hallado es mayor o igual a 50 entonces el volumen es correcto
if (volumen_correcto == True):
    print("EL VOLUMEN ES CORRECTO")
else:
    print("EL VOLUMEN ES INCORRECTO")

#fin_if
