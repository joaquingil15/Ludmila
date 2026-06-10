#Grupo 7 Casaro Federico, Gil Joaquin, Rodio Leonel y Linares Faustina

import random

#Funciones
def separador():
    print()
    print("------------------------------------")
    print()

def validar_repetidos(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return -1
    return 1

def cargar_numeros_random(lista):
    i = 1
    n = random.randint(1,9)
    lista.append(n)
    print(lista)
    while i<3:
        n = random.randint(1,9)
        aux = validar_repetidos(lista,n)
        if aux == 1:
            lista.append(n)
            i = i + 1
    return lista

def datos_cliente():
    nombre = input("Ingrese su nombre: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()
    dni = input("Ingrese su numero de dni: ")
    while len (dni) < 8 or len (dni) > 8:
        dni = input("ERROR - Ingrese un dni válido: ")
    direccion = input("Ingrese su dirección: ").capitalize()
    telefono = input("Ingrese su número de teléfono: ")
    while len (telefono) < 8 or len (telefono) > 8:
        telefono = input("ERROR - Ingrese un número de teléfono válido: ")
    mail = input("Ingrese su mail: ").capitalize()
    return nombre, apellido, dni, direccion, telefono, mail

def crear_matriz(lista1,lista2,lista3,lista4):
    matriz = []

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║                CATÁLOGO DE PRODUCTOS                ║")
    print("╠════╦═════════════════╦════════════╦══════════════════╣")
    print("║COD ║ PRODUCTO        ║ PRECIO     ║ CANTIDAD         ║")
    print("╠════╬═════════════════╬════════════╬══════════════════╣")

    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i], lista4[i]])

        print(f"║ {lista1[i]:<2} ║ {lista2[i]:<15} ║ ${lista3[i]:<8} ║ {lista4[i]:<16} ║")

    print("╚════╩═════════════════╩════════════╩══════════════════╝")

    return matriz

def crear_matriz_2(lista1,lista2,lista3,lista4):
    matriz = []
    print("Nro Factura Dni Telefono Total ")
    for i in range(len(lista1)):
        matriz.append([lista1[i],lista2[i],lista3[i],lista4[i]])
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
               
def lista_compras(lista): 
    compra = int(input("Ingrese el codigo del producto que quiere comprar: ",))-1
    while compra < 0 or compra > 8:
        compra = int(input("Error - Ingrese el codigo del producto que quiere comprar: "))
    cantidad = int(input("Cuantos desea comprar: "))
    while cantidad<=0:
        cantidad = int(input("Error - Cuantos desea comprar: "))
    lista_cantidad[compra]+=cantidad
    return lista

def sumador_total(lista1,lista2):
    sumador = 0
    for i in range(len(lista1)):
        sumador+= lista2[i]*lista1[i]
    return sumador

def mostrar_compra(lista, matriz):
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║              PRODUCTOS COMPRADOS                ║")
    print("╠════╦═════════════════╦═══════════╦══════════════╣")
    print("║COD ║ PRODUCTO        ║ PRECIO    ║ CANTIDAD     ║")
    print("╠════╬═════════════════╬═══════════╬══════════════╣")

    for i in range(len(lista)):
        if lista[i] > 0:
            print(f"║ {matriz[i][0]:<2} ║ {matriz[i][1]:<15} ║ ${matriz[i][2]:<7} ║ {lista[i]:<12} ║")

    print("╚════╩═════════════════╩═══════════╩══════════════╝")
    print()
            
def total_prendas(lista):
     t_p = 0
     t_p = lista[0] + lista[1] + lista[2]
     return t_p
    
def total_calzado(lista):
     t_c = 0
     t_c = lista[3] + lista[4]
     return t_c

def total_accesorios(lista):
     t_a = 0
     t_a = lista[5] + lista[6] + lista[7] + lista[8]
     return t_a
     
def porcentajes(t_p, t_c, t_a):
    total = t_p + t_c + t_a

    porc_prendas = (t_p * 100) / total
    porc_calzado = (t_c * 100) / total
    porc_accesorios = (t_a * 100) / total

    return porc_prendas, porc_calzado, porc_accesorios

def promedios(lista_cantidad, lista_precios):
    total_pesos_prendas = 0
    total_pesos_calzado = 0
    total_pesos_accesorios = 0

    for i in range(3):
        total_pesos_prendas = total_pesos_prendas + lista_cantidad[i] * lista_precios[i]

    for i in range(3, 5):
        total_pesos_calzado = total_pesos_calzado + lista_cantidad[i] * lista_precios[i]

    for i in range(5, 9):
        total_pesos_accesorios = total_pesos_accesorios + lista_cantidad[i] * lista_precios[i]

    t_p = total_prendas(lista_cantidad)
    t_c = total_calzado(lista_cantidad)
    t_a = total_accesorios(lista_cantidad)

    if t_p > 0:
        prom_p = total_pesos_prendas / t_p
    else:
        prom_p = 0

    if t_c > 0:
        prom_c = total_pesos_calzado / t_c
    else:
        prom_c = 0

    if t_a > 0:
        prom_a = total_pesos_accesorios / t_a
    else:
        prom_a = 0

    return prom_p, prom_c, prom_a

def envio(total):
    print(""" Disponemos de envios a domicilio:
    CABA: $3000 / CONURBANO: $4500 / INTERIOR: $6500""")
    localidad = input("Donde quiere que sea el envio: CABA/CONURBANO/INTERIOR: ").capitalize()
    while localidad != "Caba" and localidad != "Conurbano" and localidad != "Interior":
        localidad = input("ERROR - Donde quiere que sea el envio: CABA/CONURBANO/INTERIOR: ").capitalize()
    if localidad == "Caba":
        total = total + 3000
    elif localidad == "Conurbano":
        total = total + 4500
    elif localidad == "Interior":
        total = total + 6500
    print("Se añadio costos de envio")
    return total, localidad

def seleccion(lista,lista_2,lista_3,lista_4): #recibo la lista desordenada
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                aux = lista_2[i]
                lista_2[i] = lista_2[j]
                lista_2[j] = aux
                aux = lista_3[i]
                lista_3[i] = lista_3[j]
                lista_3[j] = aux
                aux = lista_4[i]
                lista_4[i] = lista_4[j]
                lista_4[j] = aux
    return lista #devuelvo la lista ordenada

def medio_pago():
    tipo_pago = input("Como desea abonar(Debito/Efectivo/Credito): ").capitalize()
    while tipo_pago != "Debito" and tipo_pago != "Efectivo" and tipo_pago != "Credito":
        tipo_pago = input("Error - Como desea abonar(Debito/Efectivo/Credito): ").capitalize()
    return tipo_pago
  
def credito(total):
    print("Tiene hasta 24 cuotas, apartir de 3 se cobra un 5% de interes")
    cuotas = int(input("Ingrese la cantidad de cuotas: "))
    while cuotas<=0 or cuotas>24:
        cuotas = int(input("ERROR - Ingrese la cantidad de cuotas: "))
    if cuotas>3:
        subtotal = total*1.05
    else:
        subtotal = total
    return cuotas, subtotal

def busqueda_lineal(lista,dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1
    

#listas
facturas = []
l_dni = []
l_telefono = []
l_total = []


cargar_numeros_random(facturas)
for c in range(3):
    lista_codigo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_articulos = ["Remera", "Buzo", "Jean", "Botas Texanas", "Tacos", "Collar", "Anillos", "Aros", "Pulseras"]
    lista_precios = [15000, 20000, 30000, 45000, 35000, 9000, 8000, 6000, 7000]
    lista_cantidad = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #inicio de la venta

    #bienvenida
    print("✮ BIENVENIDOS A LUDMILA - TIENDA DE ROPA FEMENINA ✮")
    print("--------------------------------")

    #Datos del cliente
    nombre, apellido,dni,direccion,telefono,mail = datos_cliente()

    #Creando lista de compra
    matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)
    mostrar_matriz(matriz)

    lista_cantidad = lista_compras(lista_cantidad)

    n = input("Desea seguir comprando?(Si/No)").capitalize()

    while n == "Si":
        matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)

        lista_cantidad = lista_compras(lista_cantidad)

        n = input("Desea seguir comprando?(Si/No)").capitalize()

    total = sumador_total(lista_cantidad,lista_precios)

    mostrar_compra(lista_cantidad, matriz)

    #Envio
    e = input("Quiere envio a domicilio(Si/No): ").capitalize()
    if e == "Si":
        total, loc = envio(total)
        
    #Factura

    t_p = total_prendas(lista_cantidad)
    t_c = total_calzado(lista_cantidad)
    t_a = total_accesorios(lista_cantidad)


    if t_c>0 and t_a>0:
        total = total*0.93 #descueto del 7%
    pp, pc, pa = porcentajes(t_p, t_c, t_a)

    prom_p, prom_c, prom_a = promedios(lista_cantidad, lista_precios)

    #Tipos de pago 

    print("Su subtotal es",total,"Con que desea abonar?")

    tipo_pago = medio_pago()

    if tipo_pago == "Credito":
        cuotas, subtotal = credito(total)

    print("\n════════════ FACTURA ════════════")
    print("Numero de factura",facturas[c-1])
    print("Dni:",dni)
    print("Direccion:",direccion)
    print("Numero de telefono:",telefono)
    print("Nombre del negocio: Ludmila")
    print("Mail: ludmila@gmail.com") 
    print("Teléfono: 11 4875-8574")  
    print("CUIT: 30-68229475-7 ")
    print("____________________________")
    mostrar_compra(lista_cantidad,matriz)
    if e == "Si":
        if loc == "Caba":
            print("Se sumo el costo de envio de 3000$")
        elif loc == "Conurbano":
            print("Se sumo el costo de envio de 4500$")
        elif loc == "Interior":
            print("Se sumo el costo de envio de 6500$")
    print("El total de la compra es:", total)

    if t_p > 0:
        print("Porcentaje Prendas:", round(pp,2), "%")
        print("Promedio gastado por prenda: $", round(prom_p,2))

    if t_c > 0:
        print("Porcentaje Calzado:", round(pc,2), "%")
        print("Promedio gastado por calzado: $", round(prom_c,2))

    if t_a > 0:
        print("Porcentaje Accesorios:", round(pa,2), "%")
        print("Promedio gastado por accesorio: $", round(prom_a,2))
        
    if tipo_pago == "Credito":
        print("Subtotal",subtotal,"Valor de cada cuota:",subtotal/cuotas)
    separador()
   
   
    l_dni.append(dni)
    l_telefono.append(telefono)
    l_total.append(total)


seleccion(facturas,l_dni,l_telefono,l_total)
usuarios = crear_matriz_2(facturas,l_dni,l_telefono,l_total)
mostrar_matriz(usuarios)

print("Facturas:", facturas)


num_fact = int(input("Ingrese el codigo de la factura que quiere buscar: "))
posicion = busqueda_lineal(facturas,num_fact)
if posicion == -1:
    num_fact = int(input("ERROR Al ENCONTRA - Ingrese el codigo de la factura que quiere buscar: "))
    posicion = busqueda_lineal(facturas,num_fact)
else:
    print("Factura encontrada en la posicion:", posicion)
    print("Factura:", usuarios[posicion])

