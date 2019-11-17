import os
#declarar variables
Boligrafo,Cuaderno,Corrector=0,0,0

#INPUT
Boligrafo=int(os.sys.argv[1])
Cuaderno=int(os.sys.argv[2])
Corrector=int(os.sys.argv[3])

#PROCESSING
total =(Boligrafo + Cuaderno + Corrector)

#VERIFICADOR
compra_excesiva=(total>90)

#OUTPUT
print ( " ############################################# " )
print ( " # LIBRERIA AMYS " )
print ( " ############################################# " )
print ( " #Boligrafo: " , Boligrafo)
print ( " #Cuaderno: " , Cuaderno)
print ( " #Corrector: " , Corrector)

#condicional simple
#si el comensal es compulsivo mostrarle que ha ganado un descuento
if(compra_excesiva==False):
    print("No obtuvo ningun descuento")

#fin_if
