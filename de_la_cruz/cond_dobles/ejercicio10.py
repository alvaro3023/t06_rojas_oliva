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

#condicional doble
#si el cliente es compulsivo mostrarle que ha ganado un labial o un esmalte
if(compra_excesiva==True):
    print("Usted ha ganado un labial")
else:
    print("Usted a ganado un esmalte")

#fin_if
