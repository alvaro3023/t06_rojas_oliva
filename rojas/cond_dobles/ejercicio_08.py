import os
#BOLETA DEL CINE
#DECLARAR VARIABLES
nombre_cine,fecha,cliente,nombre_pelicula,costo_pelicula,costo_combo_cine="","","","",0.0,0.0

#INPUT
nombre_cine=os.sys.argv[1]
fecha=os.sys.argv[2]
cliente=os.sys.argv[3]
nombre_pelicula=os.sys.argv[4]
n_entradas =int(os.sys.argv[5])
costo_entrada=float(os.sys.argv[6])
costo_combo_cine=float(os.sys.argv[7])

#PROCESSING
costo_total_entrada = n_entradas*costo_entrada
gasto_total=(costo_combo_cine + costo_total_entrada)

#VERIFICADOR
gasto_total_verificado = (gasto_total <= 100)
fecha_ganadora = (fecha == "12/11/2019")

print("                                                      ")
#OUTPUT
print("#####################" + " " + nombre_cine +" ######################")
print("###########################################")
print("R.U.C: 28739471634")
print("cliente:  " + cliente +     "   caja:3982872 "  + "      cajera: Leslye " )
print("################BOLETA DE VENTA#####################")
print("#pelicula: " + nombre_pelicula + "            N° sala:6  ")
print("#Descripcion     " + "  #cantidad" +  "    #precio   " )
print("#entrada  " + "            "+ str(n_entradas) + "           "  + str(costo_total_entrada))
print("combo             "  +"    1           "  + str(costo_combo_cine))
print("TOTAL............................ " + str(gasto_total))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("fecha de emision:" + str(fecha)    + "              hora: 16:45 pm" )

#CONDICIONAL SIMPLE
#SI EL PRECIO ES MENOR O IGUAL A 100 ENTONCES GANA UN REFRESCO MAS
if(gasto_total_verificado == True):
    print("USTED A GANADO UN REFRESCO")
#SI LA FECHA ES IGUAL A 12/11/2019 ENTONCES GANA UN DESCUENTO
if(fecha_ganadora == True):
     print("USTED A GANADO UN DESCUENTO")
#fin_if

