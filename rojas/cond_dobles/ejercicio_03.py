import os
#Hallar la Tasa de natalidad
#DECLARAR VARIABLE
nac_hombres,nac_mujeres,pob_total = 0,0,0
#INPUT
nac_hombres=int(os.sys.argv[1])
nac_mujeres=int(os.sys.argv[2])
pob_total =int(os.sys.argv[3])

#PROCESSING
tasa_natalidad = ((nac_hombres + nac_mujeres)/pob_total)*100

#VERIFICADO
tasa_natalidad_verificado =(tasa_natalidad >= 10)

#OUTPUT
print("El numero de hombres nacidos: " + str(nac_hombres))
print("el numero de mujeres nacidas " + str(nac_mujeres))
print("La poblacion total: " + str(pob_total))
print("La Tasa de Natalidad es: " + str(tasa_natalidad) + "%")


#CONDICION DOBLE
# si la tasa de natalidad hallado es mayor igual a 10% entonces esta creciendo
if (tasa_natalidad_verificado == True):
    print("LA TASA DE NATALIDAD ESTA CRECIENDO")
else:
    print("LA TASA DE NATALIDAD ESTA DECRECIENDO")

#fin_if
