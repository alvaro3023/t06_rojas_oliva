import os
#declarar variables
Cliente,precio1,precio2,precio3,precio4="",0,0,0,0

#INPUT
Cliente=os.sys.argv[1]
precio1=int(os.sys.argv[2])
precio2=int(os.sys.argv[3])
precio3=int(os.sys.argv[4])
precio4=int(os.sys.argv[5])

#PROCESSING
total =(precio1 + precio2 + precio3 + precio4)

#OUTPUT
print ( " ############################################# " )
print ( " # TIENDA DE ELECTRODOMESTICOS - CURACAO " )
print ( " ############################################# " )
print ( " #Cliente: " , Cliente)
print ( " #Olla arrocera: " , precio1)
print ( " #Licuadora: " , precio2)
print ( " #Plancha: " , precio3)
print ( " #Juego de tazas: " , precio4)

#condicional multiple
#si la compra es mayor a 200 soles mostrarle al comprador que ha ganado una jarra electrica
#si la compra esta entre 100 y 150 soles mostrarle al comprador que ha un tike para el sorteo de una moto
#si la compra es menor a 80 soles decirle que no ha ganado nada

if(total>200):
    print("usted ha ganado una jarra electrica")
if(total>=100 and total<150):
    print("usted a ganado un tike para el sorteo de una moto")
if(total<80):
    print("usted no ha ganadado nada")

#fin_if
