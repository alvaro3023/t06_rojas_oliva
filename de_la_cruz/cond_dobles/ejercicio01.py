import os
#declarar variables
Comensal,Azafata,precio1,precio2,precio3="","",0,0,0

#INPUT
Comensal=os.sys.argv[1]
Azafata=os.sys.argv[2]
precio1=int(os.sys.argv[3])
precio2=int(os.sys.argv[4])
precio3=int(os.sys.argv[5])

#PROCESSING
total =(precio1 + precio2 + precio3)

#VERIFICADOR
compra_excesiva=(total>200)

#OUTPUT
print(" ############################################# ")
print(" # CEVICHERIA - SEÑOR DELFIN ")
print(" ############################################# ")
print(" #Comensal: " , Comensal   +   " Azafata: " , Azafata)
print(" #Arroz con mariscos: " , precio1)
print(" #refresco de lima: " , precio2)
print(" #ocopa: " , precio3)
print("# Total    : ", total)

#condicional doble
#si el comensal es compulsivo mostrarle que ha ganado un descuento
#si el comensal no es compulsivo mostrarle que no tiene ningun descuento

if(compra_excesiva==True):
    print("OFERTA: usted ha ganado un descuento")
else:
    print("NO TIENES DESCUENTO")

#fin_if
