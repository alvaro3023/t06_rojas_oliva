import os
#PERIMETRO DE UN TRIANGULO
#DECLARAR VARIABLES
lado_a,lado_b,lado_c=0,0,0

#INPUT
lado_a =int(os.sys.argv[1])
lado_b =int(os.sys.argv[2])
lado_c =int(os.sys.argv[3])

#PROCESSING
perimetro = (lado_a + lado_b + lado_c)

#VERIFICADOR
perimetro_verificado = (perimetro < 200)

#OUTPUT
print("El valor del lado a es: " + str(lado_a))
print("El valor del lado b es: " + str(lado_b))
print("El valor del lado c es: " + str(lado_c))
print("El perimetro de un triangulo es: " + str(perimetro))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

#CONDICIONAL SIMPLE
#SI EL PERIMETRO ES MENOR  DE 200 ENTONCES ES CORRECTO
if (perimetro_verificado== True):
  print("¡MUY BIEN, EL PERIMETRO ES CORRECTO!")

else:
  print("EL PERIMETRO ES INCORRECTO")

#fin_if
