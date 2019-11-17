import os
#declarar variables
DNI,monto1,monto2,monto3,monto4=0,0,0,0,0

#INPUT
DNI=int(os.sys.argv[1])
monto1=int(os.sys.argv[2])
monto2=int(os.sys.argv[3])
monto3=int(os.sys.argv[4])
monto4=int(os.sys.argv[5])

#PROCESSING
Total_excesivo=(monto1 + monto2 + monto3 + monto4)

#VERIFICADOR
Precio_excesivo=(Total_excesivo>210)
precio_excesivo=(Total_excesivo>150)

#OUTPUT
print ( " ############################################# " )
print ( " # HIPERBODEGA - PRECIO UNO   " )
print ( " ############################################# " )
print ( " #DNI: " , DNI )
print ( " #polo: " , monto1)
print ( " #casaca: " , monto2)
print ( " #chompa: " , monto3)
print ( " #galletas: " , monto4)

#condicional doble
#si la compra es mayor de 210 gana el 20% de descuento
#si la compra es mayor de 150 gana el 10% de descuento

if(compra_excesiva==True):
    print("Ganaste el 20% de descuento")
else:
    print("Ganaste el 10% de descuento")

#fin_if
