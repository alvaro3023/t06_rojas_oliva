import os
#BOLETA DE VENTA
#DECLARAR VARIABLES
cliente,costo_ducha,costo_ceramica,costo_innodoro="",0.0,0.0,0.0

#INPUT
cliente=os.sys.argv[1]
costo_ducha=float(os.sys.argv[2])
costo_innodoro=float(os.sys.argv[3])
costo_ceramica=float(os.sys.argv[4])

#PROCESSING
monto_total=(round(costo_ducha+costo_ceramica+costo_innodoro,2))

#VERIFICADOR
monto_total_verificado=(monto_total>=60)



#OUTPUT
print("##################### PROMART CENTER ####################")
print("cliente  " + cliente )
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("producto     "  +  "       precio   " )
print("ceramica   " + "          " + str(costo_ceramica))
print("ducha                "  + str(costo_ducha))
print("innodoro             "  + str(costo_innodoro))
print("monto total:        s/" + str(monto_total))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
#CONDICIONAL SIMPLE
#SI EL MONTO ES MAYOR O IGUAL QUE 100 SOLES GANA UN VALE DE DESCUENTO
if (monto_total_verificado == True):
    print("GANASTE UN VALE DE DESCUENTO ")
#fin_if



