import os
#declarar variables
cliente,cajero,P1,P2="","",0,0
comprador_compulsivo=False

#INPUTN4
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
P1=int(os.sys.argv[3])
P2=int(os.sys.argv[4])

# PROCESSING
total = (P1 + P2)

# OUTPUT
print("#######################")
print("# FERRERTERIA - DON CHANITO")
print("#######################")
print("# Cliente:  ", cliente, "cajero:", cajero)
print("# Cemento: ",P1)
print("# Pintura: ",P2)
print("# Total  :  S/.", total)
print("#######################")

#condicional multiple
#si la compra es mayor a 150 soles mostrarle al comprador que ha ganado 2 bolsas de cemento
#si la compra esta entre 80 y 150 soles mostrarle al comprador que ha ganado un balde de pintura blanca
#si la compra es menor a 80 soles decirle que no ha ganado nada

if(total>150):
    print("usted ha ganado 2 bolsas de cemento")
if(total>=80 and total<150):
    print("usted a ganado un un balde de pintura blanca")
if(total<100):
    print("usted no ha ganadado nada")

#fin-if
