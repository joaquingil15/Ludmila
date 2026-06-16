# ============================================================
# SISTEMA DE VENTAS - TIENDA "LUDMILA" (ROPA FEMENINA)
# Grupo 7: Casaro Federico, Gil Joaquin, Rodio Leonel, Linares Faustina
# ============================================================

import random  # Importa el módulo random para generar números aleatorios


# ─────────────────────────────────────────────
# FUNCIÓN: validar_repetidos
# Verifica si un número ya existe en la lista
# Retorna -1 si está repetido, 1 si no está
# ─────────────────────────────────────────────
def validar_repetidos(lista, n):
    for i in range(len(lista)):   # Recorre todos los elementos de la lista
        if lista[i] == n:         # Si encuentra el número 'n' en la lista...
            return -1             # ...retorna -1 (está repetido)
    return 1                      # Si no lo encontró, retorna 1 (no está repetido)


# ─────────────────────────────────────────────
# FUNCIÓN: cargar_numeros_random
# Carga 3 números aleatorios únicos (del 1 al 9)
# en la lista 'facturas' para usar como nros. de factura
# ─────────────────────────────────────────────
def cargar_numeros_random(lista):
    i = 1                              # Contador: ya vamos a tener 1 número al inicio
    n = random.randint(1, 9)           # Genera el primer número aleatorio entre 1 y 9
    lista.append(n)                    # Lo agrega a la lista
    print(lista)                       # Muestra la lista con el primer número
    while i < 3:                       # Repite hasta tener 3 números en total
        n = random.randint(1, 9)       # Genera un nuevo número aleatorio
        aux = validar_repetidos(lista, n)  # Verifica si ya existe en la lista
        if aux == 1:                   # Si NO está repetido...
            lista.append(n)            # ...lo agrega a la lista
            i = i + 1                  # ...incrementa el contador
    return lista                       # Retorna la lista con 3 números únicos


# ─────────────────────────────────────────────
# FUNCIÓN: datos_cliente
# Solicita y valida los datos personales del cliente
# Retorna: nombre, apellido, dni, dirección, teléfono, mail
# ─────────────────────────────────────────────
def datos_cliente():
    nombre = input("Ingrese su nombre: ").capitalize()       # Pide nombre y capitaliza la primera letra
    apellido = input("Ingrese su apellido: ").capitalize()   # Pide apellido y capitaliza
    dni = input("Ingrese su número de dni: ")                # Pide el DNI
    while len(dni) < 8 or len(dni) > 8:                     # Valida que el DNI tenga exactamente 8 dígitos
        dni = input("ERROR - Ingrese un dni válido: ")       # Si no, pide ingresarlo de nuevo
    direccion = input("Ingrese su dirección: ").capitalize() # Pide dirección y capitaliza
    telefono = input("Ingrese su número de teléfono, sin incluir su código de área: ")  # Pide teléfono
    while len(telefono) < 8 or len(telefono) > 8:           # Valida que el teléfono tenga exactamente 8 dígitos
        telefono = input("ERROR - Ingrese un número de teléfono válido, sin incluir su código de área: ")
    mail = input("Ingrese su mail: ").capitalize()           # Pide el mail y capitaliza
    return nombre, apellido, dni, direccion, telefono, mail  # Retorna todos los datos


# ─────────────────────────────────────────────
# FUNCIÓN: crear_matriz
# Arma la matriz (tabla) de productos combinando
# 4 listas: código, nombre, precio y cantidad
# También imprime el catálogo con formato visual
# ─────────────────────────────────────────────
def crear_matriz(lista1, lista2, lista3, lista4):
    print()
    print("-------------------------------------------")
    print("A CONTINUACIÓN LES DEJAMOS TODA LA INFORMACIÓN SOBRE NUESTROS PRODUCTOS")
    print()
    matriz = []   # Lista vacía que va a contener filas de la tabla

    # Imprime el encabezado del catálogo con caracteres especiales (╔, ║, etc.)
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║                CATÁLOGO DE PRODUCTOS                ║")
    print("╠════╦═════════════════╦════════════╦══════════════════╣")
    print("║COD ║ PRODUCTO        ║ PRECIO     ║ CANTIDAD         ║")
    print("╠════╬═════════════════╬════════════╬══════════════════╣")

    for i in range(len(lista1)):                        # Recorre cada producto
        matriz.append([lista1[i], lista2[i], lista3[i], lista4[i]])  # Agrega una fila [cod, nombre, precio, cant]
        # Imprime cada fila con formato alineado usando f-strings y :<N para padding
        print(f"║ {lista1[i]:<2} ║ {lista2[i]:<15} ║ ${lista3[i]:<8} ║ {lista4[i]:<16} ║")

    print("╚════╩═════════════════╩════════════╩══════════════════╝")

    return matriz   # Retorna la matriz con todos los productos


# ─────────────────────────────────────────────
# FUNCIÓN: crear_matriz_2
# Arma la matriz de facturas con:
# nro de factura, DNI, teléfono, total
# (No imprime tabla formateada, solo texto plano)
# ─────────────────────────────────────────────
def crear_matriz_2(lista1, lista2, lista3, lista4):
    matriz = []
    print("Nro Factura Dni Telefono Total ")   # Encabezado simple
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i], lista4[i]])  # Agrega fila con los 4 datos
    return matriz


# ─────────────────────────────────────────────
# FUNCIÓN: mostrar_matriz
# Imprime cada fila de una matriz (lista de listas)
# ─────────────────────────────────────────────
def mostrar_matriz(matriz):
    for i in range(len(matriz)):  # Recorre cada fila
        print(matriz[i])          # Imprime la fila completa


# ─────────────────────────────────────────────
# FUNCIÓN: lista_compras
# Permite al cliente elegir un producto y cantidad
# Acumula la cantidad elegida en lista_cantidad (variable global)
# ─────────────────────────────────────────────
def lista_compras(lista):
    print()
    print("-----------------------------------")
    print("AGREGUE AL CARRITO LO QUE GUSTE")
    print()
    compra = int(input("Ingrese el código del producto que quiere comprar: ")) - 1  # Le resta 1 para convertir a índice 0-based
    while compra < 0 or compra > 8:                                                  # Valida que el código esté entre 1 y 9 (índice 0-8)
        compra = int(input("ERROR - Ingrese el código del producto que quiere comprar: "))
    cantidad = int(input("¿Cuántos productos de dicha categoría quiere comprar?: "))  # Pide cantidad
    while cantidad <= 0:                                                               # Valida que sea positiva
        cantidad = int(input("ERROR - ¿Cuántos productos de dicha categoría quiere comprar?: "))
    lista_cantidad[compra] += cantidad   # Suma la cantidad al acumulador de ese producto (variable global)
    return lista


# ─────────────────────────────────────────────
# FUNCIÓN: sumador_total
# Calcula el total de la compra:
# suma (precio * cantidad) para cada producto
# ─────────────────────────────────────────────
def sumador_total(lista1, lista2):
    sumador = 0                          # Acumulador inicializado en 0
    for i in range(len(lista1)):
        sumador += lista2[i] * lista1[i]  # Precio * Cantidad de cada producto
    return sumador                        # Retorna el total


# ─────────────────────────────────────────────
# FUNCIÓN: mostrar_compra
# Imprime solo los productos comprados (cantidad > 0)
# con formato visual igual al catálogo
# ─────────────────────────────────────────────
def mostrar_compra(lista, matriz):
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║              PRODUCTOS COMPRADOS                ║")
    print("╠════╦═════════════════╦═══════════╦══════════════╣")
    print("║COD ║ PRODUCTO        ║ PRECIO    ║ CANTIDAD     ║")
    print("╠════╬═════════════════╬═══════════╬══════════════╣")

    for i in range(len(lista)):        # Recorre todos los productos
        if lista[i] > 0:               # Solo muestra los que tienen cantidad mayor a 0
            print(f"║ {matriz[i][0]:<2} ║ {matriz[i][1]:<15} ║ ${matriz[i][2]:<7} ║ {lista[i]:<12} ║")

    print("╚════╩═════════════════╩═══════════╩══════════════╝")
    print()


# ─────────────────────────────────────────────
# FUNCIÓN: total_prendas
# Suma la cantidad total de prendas compradas
# (índices 0, 1, 2 → Remera, Buzo, Jean)
# ─────────────────────────────────────────────
def total_prendas(lista):
    t_p = 0
    t_p = lista[0] + lista[1] + lista[2]  # Suma cantidades de Remera, Buzo y Jean
    return t_p


# ─────────────────────────────────────────────
# FUNCIÓN: total_calzado
# Suma la cantidad total de calzado comprado
# (índices 3, 4 → Botas Texanas, Tacos)
# ─────────────────────────────────────────────
def total_calzado(lista):
    t_c = 0
    t_c = lista[3] + lista[4]  # Suma cantidades de Botas Texanas y Tacos
    return t_c


# ─────────────────────────────────────────────
# FUNCIÓN: total_accesorios
# Suma la cantidad total de accesorios comprados
# (índices 5, 6, 7, 8 → Collar, Anillos, Aros, Pulseras)
# ─────────────────────────────────────────────
def total_accesorios(lista):
    t_a = 0
    t_a = lista[5] + lista[6] + lista[7] + lista[8]  # Suma cantidades de accesorios
    return t_a


# ─────────────────────────────────────────────
# FUNCIÓN: porcentajes
# Calcula qué % del total comprado corresponde
# a prendas, calzado y accesorios
# ─────────────────────────────────────────────
def porcentajes(t_p, t_c, t_a):
    total = t_p + t_c + t_a              # Total de unidades compradas
    porc_prendas = (t_p * 100) / total   # % de prendas sobre el total
    porc_calzado = (t_c * 100) / total   # % de calzado sobre el total
    porc_accesorios = (t_a * 100) / total  # % de accesorios sobre el total
    return porc_prendas, porc_calzado, porc_accesorios


# ─────────────────────────────────────────────
# FUNCIÓN: promedios
# Calcula el precio promedio pagado por unidad
# en cada categoría (prendas, calzado, accesorios)
# ─────────────────────────────────────────────
def promedios(lista_cantidad, lista_precios):
    total_pesos_prendas = 0      # Acumulador de $ gastado en prendas
    total_pesos_calzado = 0      # Acumulador de $ gastado en calzado
    total_pesos_accesorios = 0   # Acumulador de $ gastado en accesorios

    for i in range(3):           # Índices 0, 1, 2 → prendas
        total_pesos_prendas = total_pesos_prendas + lista_cantidad[i] * lista_precios[i]

    for i in range(3, 5):        # Índices 3, 4 → calzado
        total_pesos_calzado = total_pesos_calzado + lista_cantidad[i] * lista_precios[i]

    for i in range(5, 9):        # Índices 5, 6, 7, 8 → accesorios
        total_pesos_accesorios = total_pesos_accesorios + lista_cantidad[i] * lista_precios[i]

    t_p = total_prendas(lista_cantidad)      # Total de unidades de prendas
    t_c = total_calzado(lista_cantidad)      # Total de unidades de calzado
    t_a = total_accesorios(lista_cantidad)   # Total de unidades de accesorios

    # Evita división por cero: si no compró nada en una categoría, promedio = 0
    if t_p > 0:
        prom_p = total_pesos_prendas / t_p   # Promedio $ por prenda
    else:
        prom_p = 0

    if t_c > 0:
        prom_c = total_pesos_calzado / t_c   # Promedio $ por calzado
    else:
        prom_c = 0

    if t_a > 0:
        prom_a = total_pesos_accesorios / t_a  # Promedio $ por accesorio
    else:
        prom_a = 0

    return prom_p, prom_c, prom_a


# ─────────────────────────────────────────────
# FUNCIÓN: envio
# Pregunta si el cliente quiere envío y agrega
# el costo según la zona elegida
# Retorna: total actualizado y localidad
# ─────────────────────────────────────────────
def envio(total):
    print()
    print("----------------------------------")
    print("""DISPONEMOS DE ENVÍOS A DOMICILIO
    - Caba --> $3000
    - Conurbano --> $4500
    - Interior --> $6500 """)
    localidad = input("Elija la zona de envío --> Caba/ Conurbano/ Interior: ").capitalize()
    while localidad != "Caba" and localidad != "Conurbano" and localidad != "Interior":  # Valida la zona
        localidad = input("ERROR - Elija la zona de envío --> Caba/ Conurbano/ Interior: ").capitalize()
    if localidad == "Caba":           # Si eligió CABA...
        total = total + 3000          # ...suma $3000
    elif localidad == "Conurbano":    # Si eligió Conurbano...
        total = total + 4500          # ...suma $4500
    elif localidad == "Interior":     # Si eligió Interior...
        total = total + 6500          # ...suma $6500
    print()
    print("- Se han añadido los costos de envío")
    return total, localidad           # Retorna el nuevo total y la localidad elegida


# ─────────────────────────────────────────────
# FUNCIÓN: seleccion
# Ordena la lista de facturas de menor a mayor
# usando el algoritmo de ORDENAMIENTO POR SELECCIÓN
# Mueve en paralelo las otras 3 listas para mantener coherencia
# ─────────────────────────────────────────────
def seleccion(lista, lista_2, lista_3, lista_4):
    for i in range(len(lista) - 1):       # Recorre desde el primer al anteúltimo elemento
        for j in range(i + 1, len(lista)):  # Compara con todos los siguientes
            if lista[i] > lista[j]:         # Si el actual es mayor que el siguiente...
                # Intercambia en lista principal (facturas)
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                # Intercambia en lista de DNIs (mantiene correspondencia)
                aux = lista_2[i]
                lista_2[i] = lista_2[j]
                lista_2[j] = aux
                # Intercambia en lista de teléfonos
                aux = lista_3[i]
                lista_3[i] = lista_3[j]
                lista_3[j] = aux
                # Intercambia en lista de totales
                aux = lista_4[i]
                lista_4[i] = lista_4[j]
                lista_4[j] = aux
    return lista   # Retorna la lista de facturas ordenada


# ─────────────────────────────────────────────
# FUNCIÓN: medio_pago
# Solicita y valida el método de pago elegido
# Retorna: "Debito", "Efectivo" o "Credito"
# ─────────────────────────────────────────────
def medio_pago():
    print()
    print("---------------------------")
    print("EN EL SIGUIENTE PASO, REALICE EL PAGO")
    tipo_pago = input("¿Cuál será su método de pago? --> Debito/ Efectivo/ Credito: ").capitalize()
    while tipo_pago != "Debito" and tipo_pago != "Efectivo" and tipo_pago != "Credito":  # Valida la opción
        tipo_pago = input("ERROR - ¿Cuál será su método de pago? --> Debito/Efectivo/Credito: ").capitalize()
    return tipo_pago


# ─────────────────────────────────────────────
# FUNCIÓN: credito
# Calcula el total con interés si hay más de 3 cuotas
# A partir de 3 cuotas → aplica 5% de interés
# Retorna: cantidad de cuotas y subtotal final
# ─────────────────────────────────────────────
def credito(total):
    print()
    print("---------------------------")
    print("A TENER EN CUENTA")
    print("Ofrecemos hasta 24 cuotas, pero a partir de 3 cuotas se aplica un 5% de interés en toda la compra.")
    cuotas = int(input("Ingrese la cantidad de cuotas que desea: "))
    while cuotas <= 0 or cuotas > 24:         # Valida que esté entre 1 y 24
        cuotas = int(input("ERROR - Ingrese la cantidad de cuotas que desea: "))
    if cuotas > 3:                             # Si son más de 3 cuotas...
        subtotal = total * 1.05                # ...aplica 5% de interés
    else:
        subtotal = total                       # Sin interés si son 1, 2 o 3 cuotas
    return cuotas, subtotal


# ─────────────────────────────────────────────
# FUNCIÓN: busqueda_lineal
# Busca un dato en una lista recorriéndola elemento por elemento
# Retorna el índice si lo encuentra, -1 si no está
# ─────────────────────────────────────────────
def busqueda_lineal(lista, dato):
    for i in range(len(lista)):   # Recorre toda la lista
        if lista[i] == dato:      # Si encuentra el dato...
            return i              # ...retorna su posición (índice)
    return -1                     # Si no lo encontró, retorna -1


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Listas globales para almacenar datos de los 3 clientes
facturas = []      # Lista que almacenará los 3 números de factura únicos
l_dni = []         # Lista para guardar DNI de cada cliente
l_telefono = []    # Lista para guardar teléfono de cada cliente
l_total = []       # Lista para guardar total de compra de cada cliente

# Genera 3 números de factura únicos y los carga en 'facturas'
cargar_numeros_random(facturas)

# Bucle principal: se repite 3 veces (un cliente por iteración)
for c in range(3):
    # Inicializa las listas de productos para cada cliente
    lista_codigo = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                             # Códigos del 1 al 9
    lista_articulos = ["Remera", "Buzo", "Jean", "Botas Texanas", "Tacos",                  # Nombres de productos
                       "Collar", "Anillos", "Aros", "Pulseras"]
    lista_precios = [15000, 20000, 30000, 45000, 35000, 9000, 8000, 6000, 7000]             # Precios correspondientes
    lista_cantidad = [0, 0, 0, 0, 0, 0, 0, 0, 0]                                            # Cantidades en 0 al inicio

    print("✮ BIENVENIDOS A LUDMILA - TIENDA DE ROPA FEMENINA ✮")
    print("--------------------------------")

    # Recolecta los datos del cliente
    nombre, apellido, dni, direccion, telefono, mail = datos_cliente()

    # Crea y muestra el catálogo como tabla (matriz)
    matriz = crear_matriz(lista_codigo, lista_articulos, lista_precios, lista_cantidad)
    mostrar_matriz(matriz)

    # Primera compra obligatoria
    lista_cantidad = lista_compras(lista_cantidad)

    # Pregunta si quiere seguir comprando → bucle mientras diga "Si"
    n = input("¿Desea seguir comprando? --> Si/No: ").capitalize()
    while n == "Si":
        matriz = crear_matriz(lista_codigo, lista_articulos, lista_precios, lista_cantidad)  # Actualiza el catálogo con cantidades
        lista_cantidad = lista_compras(lista_cantidad)                                        # Permite agregar más productos
        n = input("¿Desea seguir comprando? --> Si/No: ").capitalize()

    # Calcula el total de la compra (suma precio * cantidad de cada producto)
    total = sumador_total(lista_cantidad, lista_precios)

    # Muestra resumen de lo comprado
    mostrar_compra(lista_cantidad, matriz)

    # Pregunta si desea envío a domicilio
    e = input("¿Desea el envío de los productos a domicilio? --> Si/No: ").capitalize()
    if e == "Si":
        total, loc = envio(total)   # Agrega el costo de envío y guarda la localidad en 'loc'

    # Calcula totales por categoría
    t_p = total_prendas(lista_cantidad)      # Total unidades de prendas
    t_c = total_calzado(lista_cantidad)      # Total unidades de calzado
    t_a = total_accesorios(lista_cantidad)   # Total unidades de accesorios

    # DESCUENTO: si compró calzado Y accesorios → aplica 7% de descuento (multiplica por 0.93)
    if t_c > 0 and t_a > 0:
        total = total * 0.93

    # Calcula porcentajes por categoría
    pp, pc, pa = porcentajes(t_p, t_c, t_a)

    # Calcula promedios de precio por categoría
    prom_p, prom_c, prom_a = promedios(lista_cantidad, lista_precios)

    # Muestra subtotal e informa método de pago
    print("- Su subtotal es", total, ". Con qué medio de pago desea abonar?")

    tipo_pago = medio_pago()   # Obtiene el método de pago elegido

    # Si pagó con crédito, calcula cuotas e interés
    if tipo_pago == "Credito":
        cuotas, subtotal = credito(total)

    # ──────────────────────────────────────
    # IMPRIME LA FACTURA COMPLETA
    # ──────────────────────────────────────
    print("\n════════════ FACTURA ════════════")
    print("Numero de factura", facturas[c - 1])   # Número de factura (nota: c-1 puede dar índice -1 en la primera iteración)
    print("Nombre del cliente", nombre)
    print("Apellido del cliente", apellido)
    print("Dni:", dni)
    print("Direccion:", direccion)
    print("Numero de telefono:", telefono)
    print("Nombre del negocio: Ludmila")
    print("Mail: ludmila@gmail.com")
    print("Teléfono: 11 4875-8574")
    print("CUIT: 30-68229475-7 ")
    print()
    print("-----------------------------")
    mostrar_compra(lista_cantidad, matriz)   # Muestra de nuevo los productos comprados

    # Muestra costo de envío si correspondía
    if e == "Si":
        if loc == "Caba":
            print("Se sumó el costo de envío de $3000")
        elif loc == "Conurbano":
            print("Se sumó el costo de envío de $4500")
        elif loc == "Interior":
            print("Se sumó el costo de envío de $6500")

    print("El total de la compra es:", total)

    # Muestra estadísticas de prendas (solo si compró alguna)
    if t_p > 0:
        print("Porcentaje de prendas:", round(pp, 2), "%")
        print("Promedio gastado en prendas: $", round(prom_p, 2))

    # Muestra estadísticas de calzado (solo si compró alguno)
    if t_c > 0:
        print("Porcentaje Calzado:", round(pc, 2), "%")
        print("Promedio gastado en calzado: $", round(prom_c, 2))

    # Muestra estadísticas de accesorios (solo si compró alguno)
    if t_a > 0:
        print("Porcentaje Accesorios:", round(pa, 2), "%")
        print("Promedio gastado en accesorios: $", round(prom_a, 2))

    # Si pagó con crédito, muestra el subtotal con interés y el valor de cada cuota
    if tipo_pago == "Credito":
        print("- Subtotal", subtotal,
              "- Valor de cada cuota: $", subtotal / cuotas)

    # Guarda los datos del cliente en las listas globales
    l_dni.append(dni)           # Agrega el DNI a la lista de DNIs
    l_telefono.append(telefono) # Agrega el teléfono
    l_total.append(total)       # Agrega el total de compra

# ──────────────────────────────────────────────────────────
# DESPUÉS DEL BUCLE: Ordenamiento y búsqueda de facturas
# ──────────────────────────────────────────────────────────

# Ordena todas las listas paralelamente por número de factura (de menor a mayor)
seleccion(facturas, l_dni, l_telefono, l_total)

# Crea la matriz de usuarios (factura, DNI, teléfono, total) y la muestra
usuarios = crear_matriz_2(facturas, l_dni, l_telefono, l_total)
mostrar_matriz(usuarios)

print("Facturas:", facturas)
print("----------------------------")
print("BÚSQUEDA DE FACTURA")
print()

# Busca una factura por su número ingresado por el usuario
num_fact = int(input("Ingrese el código de la factura que busca: "))
posicion = busqueda_lineal(facturas, num_fact)   # Aplica búsqueda lineal
if posicion == -1:                               # Si no se encontró...
    num_fact = int(input("ERROR FACTURA INVÁLIDA - Ingrese el código de la factura busca: "))
else:                                            # Si se encontró...
    print("Factura encontrada en la posición:", posicion)  # Muestra en qué índice está
    print("Factura:", usuarios[posicion])                  # Muestra los datos de esa factura

print("-------------------------------------")
print("¡MUCHAS GRACIAS POR SU COMPRA, LOS ESPERAMOS NUEVAMENTE!")