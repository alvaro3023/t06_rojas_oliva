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

#VERIFICADOR
compra_excesiva=(total>100)

#OUTPUT
print ( " ############################################# " )
print ( " # SASTERIA EL BUEN VESTIR " )
print ( " ############################################# " )
print ( " #Camisa: " , valor1)
print ( " #Saco: " , valor2)
print ( " #Corbata: " , valor3)
print ( " #Chaleco: " , valor4)

#condicional doble
#si el comprador es compulsivo ganara una prenda camisa o pantalon

if(compra_excesiva==True):
    print("OFERTA:Ganaste una camisa")
else:
    print("OFERTA:Ganaste un pantalon")

#fin-if
