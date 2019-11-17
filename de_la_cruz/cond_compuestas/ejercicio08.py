import os
#declarar variables
Paracetamol,Hibuprofeno,Diclofenaco=0,0,0

#INPUT
Paracetamol=int(os.sys.argv[1])
Hibuprofeno=int(os.sys.argv[2])
Diclofenaco=int(os.sys.argv[3])

#PROCESSING
total=(Paracetamol + Hibuprofeno + Diclofenaco)

#OUTPUT
print ( " ############################################# " )
print ( " # BOTICA INKAFARMA " )
print ( " ############################################# " )
print ( " #Paracetamol: " , Paracetamol)
print ( " #Hibuprofeno: " , Hibuprofeno)
print ( " #Diclofenaco: " , Diclofenaco)

#condicional multiple
#si la compra es mayor a 90 soles mostrarle al comprador que ha ganado una canasta
#si la compra esta entre 90 y 70 soles mostrarle al comprador que ha ganado set de shampoo y acondicionador
#si la compra es menor a 70 soles decirle que no ha ganado nada

if(total>90):
    print("usted ha ganado una canasta")
if(total>=70 and total<90):
    print("usted a ganado un set de shampoo y acondicionador")
if(total<70):
    print("usted no ha ganadado nada")

#fin_if
