import os
#declarar variables
valor1,valor2,valor3,valor4=0,0,0,0

#INPUT
valor1=int(os.sys.argv[1])
valor2=int(os.sys.argv[2])
valor3=int(os.sys.argv[3])
valor4=int(os.sys.argv[4])

#PROCESSING
total =int(valor1 + valor2 + valor3 + valor4)

#OUTPUT
print ( " ############################################# " )
print ( " # SASTERIA EL BUEN VESTIR " )
print ( " ############################################# " )
print ( " #Camisa: " , valor1)
print ( " #Saco: " , valor2)
print ( " #Corbata: " , valor3)
print ( " #Chaleco: " , valor4)

#condicional multiple
#si la compra es mayor a 200 soles mostrarle al comprador que ha ganado una cena romantica
#si la compra esta entre 100 y 200 soles mostrarle al comprador que ha ganado una camisa
#si la compra es menor a 100 soles decirle que no ha ganado nada

if(total>200):
    print("usted ha ganado una cena romantica")
if(total>=100 and total<200):
    print("usted a ganado una camisa")
if(total<100):
    print("usted no ha ganadado nada")

#fin_if
