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
total =int(precio1 + precio2 + precio3)

#OUTPUT
print(" ############################################# ")
print(" # CEVICHERIA - SEÑOR DELFIN ")
print(" ############################################# ")
print(" #Comensal: " , Comensal   +   " Azafata: " , Azafata)
print(" #Arroz con mariscos: " , precio1)
print(" #refresco de lima: " , precio2)
print(" #ocopa: " , precio3)
print("# Total    : ", total)

#condicional multiple
#si el pedido es mayor a 100 soles mostrarle al comprador que ha ganado un plato de ocopa mas refresco
#si el pedido es igual a 70 soles mostrarle al comprador que ha ganado un refresco
#si el pedido es menor a 40 soles decirle que no ha ganado nada

if(total>100):
    print("usted ha ganado un plato de ocopa mas refresco")
if(total==70):
    print("usted a ganado un refresco")
if(total<40):
    print("usted no ha ganadado nada")

#fin_if
