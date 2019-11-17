import os
#Hallar  la Tasa de mortalidad
#DECLARAR VARIABLE
muerte_natural,muerte_provocada,pob_total = 0,0,0
#INPUT
muerte_provocada=int(os.sys.argv[1])
muerte_natural=int(os.sys.argv[2])
pob_total =int(os.sys.argv[3])

#PROCESSING
tasa_mortalidad =(muerte_provocada + muerte_natural)/pob_total * 100

#VERIFICADOR
tasa_mortalidad_verificado = (tasa_mortalidad <= 200)

#OUTPUT
print("Las muertes provocadas son: " + str(muerte_provocada))
print("Las muertes naturales son: " + str(muerte_natural))
print("La poblacion total es: " + str(pob_total))
print("La tasa de mortalidad es: " + str(tasa_mortalidad) + "%")
print("La tasa de mortalidad hallado es: " + str(tasa_mortalidad_verificado))

#CONDICION SIMPLE
# si la tasa de moortalidad hallado es menor o igual a 200 entonces la tasa de la mortalidad esta decreciendo
if (tasa_mortalidad_verificado == True):
    print("LA TASA DE MORTALIDAD ESTA DECRECIENDO")

#fin_if
