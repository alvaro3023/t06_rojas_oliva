import os
#DECLARAR VARIABLES
panaderia,cajero,n_cliente,pan,tarro_leche,costo_tarro_leche="","",0,0.0,0,0.0
#INPUT
panaderia=os.sys.argv[1]
cajero=os.sys.argv[2]
n_cliente=int(os.sys.argv[3])
pan=float(os.sys.argv[4])
tarro_leche=int(os.sys.argv[5])
costo_tarro_leche=float(os.sys.argv[6])


#PROCESSING
costo_total_leche=round(tarro_leche*costo_tarro_leche,2)
costo_total_venta=(round(costo_total_leche+ pan,2))

#VERIFICADOR
costo_total_venta_verificada=(costo_total_venta>=20)
n_cliente_ganador=(n_cliente>=100)

print("                                                      ")
#OUTPUT
print("################# BOLETA DE VENTA ##################")
print("##############" + "PANADERIA " + panaderia + "###################")
print("####################################################")
print("N° cliente :" + str(n_cliente) +  "                        cajero:" + cajero)
print("####################################################")
print("pedido   " +     "     cantidad   " +     "   prec.unit  "     +   "        total")
print("pan             "  + str(pan) +  "          .....             " + str(pan)   )
print("tarro de leche    "  + str(tarro_leche)   + "          "  + str(costo_tarro_leche) + "               " + str(costo_total_leche))
print("monto total:..................................." + str(costo_total_venta))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _")
#CONDICIONAL SIMPLE
#SI EL MONTO DE COMPRA SUPERA O IGUALA A 20 SOLES ENTONCES SE GANA UNA BARRA DE CHOCOLATE NAVIDEÑA
if (costo_total_venta_verificada== True):
    print("¡GANASTE UNA BARRA DE CHOCOLATE NAVIDEÑA!")

#SI EL NUMERO DE CLIENTE ES MAYOR O IGUAL 100 ERES EL CLIENTE GANADOR
if (n_cliente_ganador==True):
    print("¡ERES EL CLIENTE GANADOR!")
#fin_if
