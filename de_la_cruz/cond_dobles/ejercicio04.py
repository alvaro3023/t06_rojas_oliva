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
total =float(precio1 + precio2 + precio3 + precio4)

#VERIFICADOR
compra_excesiva=(total>180)

#OUTPUT
print ( " ############################################# " )
print ( " # TIENDA DE ELECTRODOMESTICOS - CURACAO " )
print ( " ############################################# " )
print ( " #Cliente: " , Cliente)
print ( " #Olla arrocera: " , precio1)
print ( " #Licuadora: " , precio2)
print ( " #Plancha: " , precio3)
print ( " #Juego de tazas: " , precio4)

#condicional doble
#si el monto total es mayor de 180 entra al sorteo de una canasta
#si el monto total es menor de 180 no entra al sorteo de una canasta

if(compra_excesiva==True):
    print("Entro al sorteo para una canasta")
else:
    print("Lo sentimos no entro al sorteo")

#fin_if
