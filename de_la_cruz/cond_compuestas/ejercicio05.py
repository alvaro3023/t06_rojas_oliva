import os
#declarar variables
Boligrafo,Cuaderno,Corrector=0,0,0

#INPUT
Boligrafo=int(os.sys.argv[1])
Cuaderno=int(os.sys.argv[2])
Corrector=int(os.sys.argv[3])

#PROCESSING
total =(Boligrafo + Cuaderno + Corrector)

#OUTPUT
print ( " ############################################# " )
print ( " # LIBRERIA AMYS " )
print ( " ############################################# " )
print ( " #Boligrafo: " , Boligrafo)
print ( " #Cuaderno: " , Cuaderno)
print ( " #Corrector: " , Corrector)

#condicional multiple
#si la compra es mayor a 50 soles ganara una canasta de utiles
#si la compra esta igual 30 soles entrara al sorteo de un usb
#si la compra es menor a 20 soles ganara un cuaderno

if(total>50):
    print("usted ha ganado una canasta de utiles")
if(total==30):
    print("usted a entrado al sorteo de un usb")
if(total<20):
    print("usted ha ganadado cuaderno")

#fin_if
