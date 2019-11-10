
#IMPRESION TIPO BOLETA

#INPUT
cliente=input("nombre del cliente:")
entrega1=int(input("nro de zapatillas:"))
entrega2=int(input("nro de polos:"))
entrega3=int(input("nro de short"))
pu1=float(input("precio de zapatillas:"))
pu2=float(input("precio de polos"))
pu3=float(input("precio de short"))
IGV=8.8
#PROCESSING
total=(entrega1*pu1+entrega2*pu2+entrega3*pu3)+IGV
#VERIFICADOR
verificar=(total>=562)
#OUTPUT
print("##########################")
print(" BOLETA DE VENTA : PEPITO ")
print("##########################")
print("#")
print("#cliente:            ",cliente,"      ")
print("#zapatillas:         ",entrega1,"     ")
print(" pu polos:           ",pu1,"          ")
print("#polos:              ",entrega2,"     ")

#INPUT
masa=int(input("masa:"))
velocidad=int(input("velocidad:"))
#PROCESSING
energia_cinetica=(masa*(velocidad*2))/2
print("energia cinetica:", energia_cinetica)
#VERIFICADORE
comprobar=(energia_cinetica>=43)
#OUTPUT
print("################################")
print(" ENERGIA CINETICA DE TODO CUERPO ")
print("################################")
print("#")
print("# DATOS:                VALOR:   ")
print("#masa:                ",masa,"    ")
print("#velocidad:           ",velocidad," ")
print("#energia cinetica:    ",energia_cinetica,"  ")
print("################################")
print(" comprobar la energia cinetica:",comprobar)

#INPUT
cliente=input("ingreses nombre del cliente:")
vendedor=input("ingrese nombre del vendedor:")
naranjas=int(input("ingrese la cantidad de naranjas"))
pu=float(input("ingrese precio unitario"))
#PROCESSING
total=(naranjas*pu)
#OUTPUT
print("#########################")
print("# BOLETA DE COMPRAS #")
print("# MERCADO DOÑA PELOS #")
print("# cliente:", cliente)
print("# vendedor:", vendedor)
print("# fecha: 09/11/19   Hora: 10:12 a.m")
print("# naranjas:", naranjas," centenas ")
print("# P.U:",  pu)
print("## YA NO VENGA :) ##")
print("#########################")


#INPUT
paciente=input("ingreses nombre del paciente:")
vendedor=input("ingrese nombre del vendedor:")
medicamentos=int(input("ingrese la cantidad de medicamentos"))
pu=float(input("ingrese precio unitario"))
#PROCESSING
total=(naranjas*pu)
#OUTPUT
print("#########################")
print("# BOLETA DE COMPRAS #")
print("# BOTICA MI JESUS #")
print("# paciente:", paciente)
print("# vendedor:", vendedor)
print("# fecha: 07/11/19   Hora: 6:52 a.m")
print("# medicamentos:", medicamentos," unidad ")
print("# P.U:",  pu)
print("## OJALA SE CURE WE ##")
print("#########################")


#INPUT
cliente=input("nombre del cliente:")
pedido1=int(input("nro de camisas:"))
pedido2=int(input("nro de poleras:"))
pedido3=int(input("nro de buzos"))
pu1=float(input("precio de camisas:"))
pu2=float(input("precio de poleras"))
pu3=float(input("precio de buzos"))
IGV=8.8
#PROCESSING
total=(pedido1*pu1+pedido2*pu2+pedido3*pu3)+IGV
#VERIFICADOR
verificar=(total>=562)
#OUTPUT
print("##########################")
print(" BOLETA DE COMPRA : DON PEPE ")
print("##########################")
print("#")
print("#cliente:            ",cliente,"      ")
print("#camisa:         ",pedido1,"     ")
print(" pu polos:           ",pu1,"          ")
print("#poleras:              ",pedido2,"     ")


#INPUT
peso=int(input("peso:"))
masa=int(input("masa:"))
#PROCESSING
gravedad=(peso*masa)
print("gravedad:", gravedad)
#VERIFICADOR
comprobar=(gravedad>=43)
#OUTPUT
print("################################")
print(" LA GRAVEDAD ")
print("################################")
print("#")
print("# DATOS:                VALOR:   ")
print("#peso:                ",peso,"    ")
print("#masa:           ",masa," ")
print("#gravedad:    ",gravedad,"  ")
print("################################")
print(" comprobar la gravedad: ",comprobar)

#INPUT
fuerza=int(input("fuerza:"))
distancia=int(input("distancia:"))
#PROCESSING
trabajo=fuerza*distancia
print("trabajo:",trabajo)
#VERIFICADOR
comprobar=(trabajo<=75)
#OUTPUT
print("##################################")
print(" TRABAJO DE UN CAMION ")
print("##################################")
print("#")
print("# DATOS:                VALOR:")
print("# fuerza:             ",fuerza,"     ")
print("# distancia:          ",distancia,"    ")
print("# trabajo:            ",trabajo,"      ")
print("##################################")
print(" comprobar el trabajo:", comprobar)

#INPUT
masa=int(input("masa:"))
volumen=int(input("volumen:"))
#PROCESSING
densidad=masa/volumen
print("densidad:",densidad)
#VERIFICADOR
comprobar=(densidad<=543)
#OUTPUT
print("##################################")
print(" DENSIDAD DE UN CUERPO EN AGUA ")
print("##################################")
print("#")
print("# DATOS:                VALOR:")
print("# masa:             ",masa,"     ")
print("# volumen:          ",volumen,"    ")
print("# densidad:            ",densidad,"      ")
print("##################################")
print(" comprobar la densidad:", comprobar)


#INPUT
cliente=input("ingreses nombre del cliente:")
vendedor=input("ingrese nombre del vendedor:")
sillas=int(input("ingrese la cantidad de sillas"))
pu=float(input("ingrese precio unitario"))
#PROCESSING
total=(sillas*pu)
#OUTPUT
print("#########################")
print("# BOLETA DE COMPRAS #")
print("# SODIMAC #")
print("# cliente:", cliente)
print("# vendedor:", vendedor)
print("# fecha: 08/11/19   Hora: 1:53 p.m")
print("# sillas:", medicamentos," docena ")
print("# P.U:",  pu)
print("## REGRESE PRONTO ##")
print("#########################")


#INPUT
cliente=input("ingreses nombre del cliente:")
vendedor=input("ingrese nombre del vendedor:")
dulces=int(input("ingrese la cantidad de dulces"))
pu=float(input("ingrese precio por unidad"))
#PROCESSING
total=(dulces*pu)
#OUTPUT
print("#########################")
print("# PANADERIA TODO RICO #")
print("# TODO RICO #")
print("# cliente:", cliente)
print("# vendedor:", vendedor)
print("# dulces", dulces," centenas ")
print("# P.U:",  pu)
print("## QUE TENGA BUEN DIA ##")
print("#########################")









