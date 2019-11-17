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
Promendio_aprobatorio=(promedio==20)

print("promedio:", promedio)

#condicional doble
#Si el promedio es igual 20 entonces aprobaste el bimestre
#Si el promedio es menor de 10 entonces desaprobaste el bimestre

if (promedio == True):
    print("Aprobaste el bimestre")
else:
    print("Desprobaste el bimestre")

#fin-if
