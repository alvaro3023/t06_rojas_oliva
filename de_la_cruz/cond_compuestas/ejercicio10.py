import os
#declarar variables
prod1, prod2, prod3, prod4, prod5=0,0,0,0,0

#INPUT
prod1=int(os.sys.argv[1])
prod2=int(os.sys.argv[2])
prod3=int(os.sys.argv[3])
prod4=int(os.sys.argv[4])
prod5=int(os.sys.argv[5])

#PROCESSING
total_pago =float(prod1 + prod2 + prod3 + prod4 + prod5)

#VERIFICADOR
compra_excesiva=(total_pago>120)

#OUTPUT
print(" ############################################# ")
print(" ######## UNIKE ############## ")
print(" ############################################# ")
print(" #Labial rojo: " , prod1)
print(" #Sombras: " , prod2)
print(" #Lapiz negro: " , prod3)
print(" #Base: " , prod4)
print(" #Rubor: " , prod5)

#condicional multiple
#si la compra es mayor a 100 soles gana una plancha
#si la compra esta entre 50 y 100 soles gana una cartera
#si la compra es igual 50 gana un labial

if(compra_excesiva>100):
    print("usted ha ganado una plancha")
if(compra_excesiva>50 and total<100):
    print("usted a ganado una cartera")
if(compra_excesiva==50):
    print("usted a ganado un labial")

#fin_if
