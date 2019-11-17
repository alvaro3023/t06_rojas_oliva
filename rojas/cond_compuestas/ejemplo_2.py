import os

#Hallar el area de un trapecio
#DECLARAR VARIABLE
base_mayor, base_menor, altura = 0,0,0.0
#INPUT
base_mayor =int(os.sys.argv[1])
base_menor =int(os.sys.argv[2])
altura =int(os.sys.argv[3])

#processing
area_trapecio =(base_mayor + base_menor )/2*altura

#VERIFICADOR
area_trapecio_verificado = (area_trapecio <100)

#OUTPUT
print("La base mayor de un trapecio es: " + str(base_mayor))
print("La base menor de un trapecio es: " + str(base_menor))
print("El area del trapecio es: " + str(area_trapecio))

#CONDICION DOBLE
# si el volumen hallado es menor a 100 entonces el volumen es correcto
if (area_trapecio_verificado == True):
    print("EL AREA ES CORRECTA")

if (area_trapecio>100 and area_trapecio<200):
    print("EL AREA ES INCORRECTA")

if (area_trapecio>200 and area_trapecio<=400):
    print("EL AREA ES EXTENSA")

#fin_
