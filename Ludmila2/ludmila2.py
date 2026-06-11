#Grupo 7 Casaro Federico, Gil Joaquin, Rodio Leonel y Linares Faustina

import random

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
    dni = input("Ingrese su número de dni: ")
    while len (dni) < 8 or len (dni) > 8:
        dni = input("ERROR - Ingrese un dni válido: ")
    direccion = input("Ingrese su dirección: ").capitalize()
    telefono = input("Ingrese su número de teléfono, sin incluir su código de área: ")
    while len (telefono) < 8 or len (telefono) > 8:
        telefono = input("ERROR - Ingrese un número de teléfono válido, sin incluir su código de área: ")
    mail = input("Ingrese su mail: ").capitalize()
    return nombre, apellido, dni, direccion, telefono, mail

def crear_matriz(lista1,lista2,lista3,lista4):
    print()
    print("-------------------------------------------")
    print("A CONTINUACIÓN LES DEJAMOS TODA LA INFORMACIÓN SOBRE NUESTROS PRODUCTOS")
    print()
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
    print()
    print("-----------------------------------")
    print("AGREGUE AL CARRITO LO QUE GUSTE")
    print()
    compra = int(input("Ingrese el código del producto que quiere comprar: ")) - 1
    while compra < 0 or compra > 8:
        compra = int(input("ERROR - Ingrese el código del producto que quiere comprar: "))
    cantidad = int(input("¿Cuántos productos de dicha categoría quiere comprar?: "))
    while cantidad <= 0:
        cantidad = int(input("ERROR - ¿Cuántos productos de dicha categoría quiere comprar?: "))
    lista_cantidad[compra] += cantidad
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
    print()
    print("----------------------------------")
    print("""DISPONEMOS DE ENVÍOS A DOMICILIO
    - Caba --> $3000
    - Conurbano --> $4500
    - Interior --> $6500 """)
    localidad = input("Elija la zona de envío --> Caba/ Conurbano/ Interior: ").capitalize()
    while localidad != "Caba" and localidad != "Conurbano" and localidad != "Interior":
        localidad = input("ERROR - Elija la zona de envío --> Caba/ Conurbano/ Interior: ").capitalize()
    if localidad == "Caba":
        total = total + 3000
    elif localidad == "Conurbano":
        total = total + 4500
    elif localidad == "Interior":
        total = total + 6500
    print()
    print("- Se han añadido los costos de envío")
    return total, localidad

def seleccion(lista,lista_2,lista_3,lista_4): 
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
    return lista 

def medio_pago():
    print()
    print("---------------------------")
    print("EN EL SIGUIENTE PASO, REALICE EL PAGO")
    tipo_pago = input("¿Cuál será su método de pago? --> Debito/ Efectivo/ Credito: ").capitalize()
    while tipo_pago != "Debito" and tipo_pago != "Efectivo" and tipo_pago != "Credito":
        tipo_pago = input("ERROR - ¿Cuál será su método de pago? --> Debito/Efectivo/Credito: ").capitalize()
    return tipo_pago
  
def credito(total):
    print()
    print("---------------------------")
    print("A TENER EN CUENTA")
    print("Ofrecemos hasta 24 cuotas, pero a partir de 3 cuotas se aplica un 5% de interés en toda la compra.")
    cuotas = int(input("Ingrese la cantidad de cuotas que desea: "))
    while cuotas<=0 or cuotas>24:
        cuotas = int(input("ERROR - Ingrese la cantidad de cuotas que desea: "))
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


    print("✮ BIENVENIDOS A LUDMILA - TIENDA DE ROPA FEMENINA ✮")
    print("--------------------------------")

    nombre, apellido,dni,direccion,telefono,mail = datos_cliente()

    matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)
    mostrar_matriz(matriz)

    lista_cantidad = lista_compras(lista_cantidad)

    n = input("¿Desea seguir comprando? --> Si/No: ").capitalize()
    while n == "Si":
        matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)
        lista_cantidad = lista_compras(lista_cantidad)
        n = input("¿Desea seguir comprando? --> Si/No: ").capitalize()

    total = sumador_total(lista_cantidad,lista_precios)

    mostrar_compra(lista_cantidad, matriz)

    e = input("¿Desea el envío de los productos a domicilio? --> Si/No: ").capitalize()
    if e == "Si":
        total, loc = envio(total)
        

    t_p = total_prendas(lista_cantidad)
    t_c = total_calzado(lista_cantidad)
    t_a = total_accesorios(lista_cantidad)


    if t_c>0 and t_a>0:
        total = total*0.93 
    pp, pc, pa = porcentajes(t_p, t_c, t_a)

    prom_p, prom_c, prom_a = promedios(lista_cantidad, lista_precios)


    print("- Su subtotal es",total,". Con qué medio de pago desea abonar?")

    tipo_pago = medio_pago()

    if tipo_pago == "Credito":
        cuotas, subtotal = credito(total)

    print("\n════════════ FACTURA ════════════")
    print("Numero de factura",facturas[c-1])
    print("Nombre del cliente", nombre)
    print("Apellido del cliente", apellido)
    print("Dni:",dni)
    print("Direccion:",direccion)
    print("Numero de telefono:",telefono)
    print("Nombre del negocio: Ludmila")
    print("Mail: ludmila@gmail.com") 
    print("Teléfono: 11 4875-8574")  
    print("CUIT: 30-68229475-7 ")
    print()
    print("-----------------------------")
    mostrar_compra(lista_cantidad,matriz)
    if e == "Si":
        if loc == "Caba":
            print("Se sumó el costo de envío de $3000")
        elif loc == "Conurbano":
            print("Se sumó el costo de envío de $4500")
        elif loc == "Interior":
            print("Se sumó el costo de envío de $6500")
    print("El total de la compra es:", total)

    if t_p > 0:
        print("Porcentaje de prendas:", round(pp,2), "%")
        print("Promedio gastado en prendas: $", round(prom_p,2))

    if t_c > 0:
        print("Porcentaje Calzado:", round(pc,2), "%")
        print("Promedio gastado en calzado: $", round(prom_c,2))

    if t_a > 0:
        print("Porcentaje Accesorios:", round(pa,2), "%")
        print("Promedio gastado en accesorios: $", round(prom_a,2))
        
    if tipo_pago == "Credito":
        print("- Subtotal",subtotal,
              "- Valor de cada cuota: $",subtotal/cuotas)
   
   
    l_dni.append(dni)
    l_telefono.append(telefono)
    l_total.append(total)


seleccion(facturas,l_dni,l_telefono,l_total)
usuarios = crear_matriz_2(facturas,l_dni,l_telefono,l_total)
mostrar_matriz(usuarios)

print("Facturas:", facturas)
print("----------------------------")
print("BÚSQUEDA DE FACTURA")
print()

num_fact = int(input("Ingrese el código de la factura que busca: "))
posicion = busqueda_lineal(facturas,num_fact)
if posicion == -1:
    num_fact = int(input("ERROR FACTURA INVÁLIDA - Ingrese el código de la factura busca: "))
else:
    print("Factura encontrada en la posición:", posicion)
    print("Factura:", usuarios[posicion])
    
print("-------------------------------------")   
print("¡MUCHAS GRACIAS POR SU COMPRA, LOS ESPERAMOS NUEVAMENTE!")



