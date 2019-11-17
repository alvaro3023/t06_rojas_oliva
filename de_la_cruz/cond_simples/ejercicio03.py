import os
#declarar variables
nota1,nota2,nota3=0,0,0

#input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])

#Procesing
promedio=((nota1+nota2+nota3)/3)

#verificador
Promendio_aprobatorio=(promedio>=16)

print("promedio:", promedio)

#condicional simple
#Si el pomedio es mayor o igual 20 entonces Aprobaste el bimestre
if (promedio == True):
    print("Aprobaste el bimestre")

#fin-if
