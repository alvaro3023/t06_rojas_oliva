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
#verificador
comprador_compulsivo=(total>250)

# OUTPUT
print("#######################")
print("# FERRERTERIA - DON CHANITO")
print("#######################")
print("# Cliente:  ", cliente, "cajero:", cajero)
print("# Cemento: ",P1)
print("# Pintura: ",P2)
print("# Total  :  S/.", total)
print("#######################")

#condicional doble
#si el comprador es compulsivo mostrarle la oferta de descuento
#si el comprador no es compulsivo no tendra descuento

if(comprador_compulsivo==True):
    print("Ganaste un descuento")
else:
    print("No superaste los 250 soles, no hay descuento")

#fin-if
