import os
#BOLETA DE VENTA EN ROPA
#DECLARAR VARIABLES
empresa,cajera,cliente,pantalon,costo_pantalon,polo,costo_polo,zapatos,costo_zapatos="","","",0,0.0,0,0.0,0,0.0

#INPUT
empresa=os.sys.argv[1]
cajera=os.sys.argv[2]
cliente=os.sys.argv[3]
pantalon=int(os.sys.argv[4])
costo_pantalon=float(os.sys.argv[5])
polo=int(os.sys.argv[6])
costo_polo=float(os.sys.argv[7])
zapatos=int(os.sys.argv[8])
costo_zapatos=float(os.sys.argv[9])

#PROCESSING
total_pantalon=(round(pantalon* costo_pantalon,2))
total_polo=(polo * costo_polo)
total_zapatos=(zapatos * costo_zapatos)
total_consumo=(round(total_pantalon + total_polo + total_zapatos,2))

#VERIFICADOR
total_consumo_verificado=(total_consumo >=155)

print("                                                      ")
#OUTPUT
print("#####################" + empresa + "######################")
print("############## CENCOSUD RETAIL PERU S.A##############")
print("                calle av.grau nro 589")
print("#R.U.C:87354208735  " )
print("cliente  " + cliente + "         caja:2489    " + "  cajera  " + cajera)
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("producto     " + "    cantidad    " +  "   precio   " +   "    total")
print("pantalon     " + "       " + str(pantalon)  +   "            "  +   str(costo_pantalon)  + "         "  +  str(total_pantalon))
print("polo                "  + str(polo) + "            " + str(costo_polo) + "         " + str(total_polo))
print("zapatos             "  + str(zapatos)   + "            "  + str(costo_zapatos) + "        " + str(total_zapatos))
print("monto total:............................... s/" + str(total_consumo))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("fecha de emision: 23/04/2012"     + " hora: 15:33 pm")

#CONDICIONAL SIMPLE
#SI EL MONTO TOTAL DE COMPRA ES MAYOR O IGUAL A 155 ENTONCES SE LLEVA UN POLO GRATIS
if(total_consumo_verificado == True):
    print("GANASTE UN POLO GRACIAS A TU COMPRA")
#fin_if
