import os
#declarar variables
Boligrafo,Cuaderno,Corrector=0,0,0

#INPUT
Boligrafo=int(os.sys.argv[1])
Cuaderno=int(os.sys.argv[2])
Corrector=int(os.sys.argv[3])

#PROCESSING
total =int(Boligrafo + Cuaderno + Corrector)

#VERIFICADOR
compra_excesiva=(total>90)

#OUTPUT
print ( " ############################################# " )
print ( " # LIBRERIA AMYS " )
print ( " ############################################# " )
print ( " #Boligrafo: " , Boligrafo)
print ( " #Cuaderno: " , Cuaderno)
print ( " #Corrector: " , Corrector)

#condicional doble
#si el comensal es compulsivo mostrarle que ha ganado un descuento
#si el comensal no es compulsivo mostrarle que no obtuvo ningun descuento

if(compra_excesiva==False):
    print("No obtuvo ningun descuento")
else:
    print("GANASTE UN DESCUENTO")

#fin_if
