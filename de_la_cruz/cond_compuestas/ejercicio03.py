import os
#declarar variables
nota1,nota2,nota3=0,0,0

#input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])

#Procesing
promedio=(nota1+nota2+nota3)/3

print("promedio:", promedio)

#condicional multiple
#si el promedio es igual a 20 ganas una beca al extranjero
#si el promedio es menor a 10 no ganas nada
#si el promedio es igual a 17 ganas dos libros de Programacion

if(promedio==18):
    print("usted ha ganado una beca al extranjero")
if(promedio<10):
    print("usted no a ganado nada")
if(promedio>15):
    print("usted ha ganadado dos libros de Programacion")

#fin_if
