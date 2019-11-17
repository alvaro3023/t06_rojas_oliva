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
total=(monto1 + monto2 + monto3 + monto4)

#OUTPUT
print ( " ############################################# " )
print ( " # HIPERBODEGA - PRECIO UNO   " )
print ( " ############################################# " )
print ( " #DNI: " , DNI )
print ( " #polo: " , monto1)
print ( " #casaca: " , monto2)
print ( " #chompa: " , monto3)
print ( " #galletas: " , monto4)

#condicional multiple
#si la compra es menor a 50 y mayor de 40 soles paga 3 sol mas y gana una pizza
#si la compra es igual a 80 soles gana un paquete de utiles
#si la compra es mayor a 150 soles gana un paneton, vino y aconcagua de durazno

if(total<50 and total>40):
    print("usted ha ganado una pizza")
if(total==80):
    print("usted a ganado un paquete de utiles")
if(total<100):
    print("usted no ha ganadado un paneton, vino y aconcagua de durazno")

#fin_if
