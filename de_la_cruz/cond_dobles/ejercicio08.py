import os
#declarar variables
Paracetamol,Hibuprofeno,Diclofenaco=0,0,0

#INPUT
Paracetamol=int(os.sys.argv[1])
Hibuprofeno=int(os.sys.argv[2])
Diclofenaco=int(os.sys.argv[3])

#PROCESSING
total=float(Paracetamol + Hibuprofeno + Diclofenaco)

#VERIFICADOR
compra_excesiva=(total>200)

#OUTPUT
print ( " ############################################# " )
print ( " # BOTICA INKAFARMA " )
print ( " ############################################# " )
print ( " #Paracetamol: " , Paracetamol)
print ( " #Hibuprofeno: " , Hibuprofeno)
print ( " #Diclofenaco: " , Diclofenaco)

#condicional doble
#si el comensal es compulsivo mostrarle que ha ganado un descuento
#si el comensal no es compulsivo no obtuvo un descuento

if(compra_excesiva==False):
    print("No tiene ningun descuento")
else:
    print("A tenido suerte, gano un descuento")

#fin_if
