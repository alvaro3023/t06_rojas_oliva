import os
#BOLETA DE VENTA DE ELECTRODOMESTICOS
#DECLARAR VARIABLES
empresa,cliente,radio,costo_radio,tv,costo_tv = "","",0,0.0,0,0.0
#INPUT
empresa=os.sys.argv[1]
cliente=os.sys.argv[2]
radio=int(os.sys.argv[3])
costo_radio=float(os.sys.argv[4])
tv=int(os.sys.argv[5])
costo_tv=float(os.sys.argv[6])

#PROCESSING
total_costo_radio=(radio* costo_radio)
total_costo_tv=(tv*costo_tv)
total_venta=(total_costo_radio+total_costo_tv)

#VERIFICADOR
total_venta_verificador = (total_venta >= 200)
total_costo_radio_verificado=(total_costo_radio<=450)

print("                                                      ")
#OUTPUT
print("#####################" + " " + empresa +" ######################")
print("                calle Pedro Ruiz")
print("R.U.C: 23639275843  " )
print("cliente  " + cliente + "   caja: 234 "  + "  cajero: PANFILO  " )
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("electrodomestico     " + "    cantidad    " +  "   precio   " +   "    total")
print("radio        " + "               " + str(radio)  +   "            "  +   str(costo_radio)  + "         "  +  str(total_costo_radio))
print("tv                          "  + str(tv) + "           " + str(costo_tv) + "      " + str(total_costo_tv))
print("monto total:......................................s/" + str(total_venta))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _")
print("Donde todo es más barato! ")
#CONDICIONAL SIMPLE
#SI EL  TOTAL DE VENTA ES MAYOR  O IGUAL A 200 ENTONCES GANAS  UNOS AUDIFONOS
if(total_venta_verificador == True):
    print("FELICIDADES HA GANADO UNOS AUDIFONOS")

#SI EL MONTO EN COMPRA DE LOS RADIOS ES MENOR O IGUAL A 450 ENTONCES TIENE UN DESCUENTO DEL 20% EN EL PROXIMO RADIO
if(total_costo_radio_verificado == True):
    print("USTED HA GANADO UN DESCUENTO DEL 20% EN EL SIGUIENTE ELECTRODOMÉSTICO")

#fin_if
