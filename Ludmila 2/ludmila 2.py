#Grupo 7 Casaro Federico, Gil Joaquin, Rodio Leonel y Linares Faustina

import random

#Funciones
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
    print("Codigo Producto Valor Cantidad")
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

def mostrar_compra(lista,matriz):
    for i in range(len(lista)):
        if lista[i]>0:
            print(matriz[i])

def total_calzado(lista):
     t_c = 0
     t_c = lista[3] + lista[4]
     return t_c

def total_accesorios(lista):
     t_a = 0
     t_a = lista[5] + lista[6] + lista[7] + lista[8]
     return t_a
     
def envio(total):
    print(""" Disponemos de envios a domicilio:
    CABA: $3000 / CONURBANO: $4500 / INTERIOR: $6500""")
    localidad = input("Donde quiere que sea el envio: CABA/CONURBANO/INTERIOR: ").capitalize()
    while localidad != "Caba" and localidad != "Cornurbano" and localidad != "Interior":
        localidad = input("ERROR - Donde quiere que sea el envio: CABA/CONURBANO/INTERIOR: ").capitalize()
    if localidad == "Caba":
        total = total + 3000
    elif localidad == "Cornurbano":
        total = total + 4500
    elif localidad == "Interior":
        total = total + 6500
    print("Se añadio costos de envio")
    return total

#listas
lista_codigo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_articulos = ["Remera", "Buzo", "Jean", "Botas Texanas", "Tacos", "Collar", "Anillos", "Aros", "Pulseras"]
lista_precios = [15000, 20000, 30000, 45000, 35000, 9000, 8000, 6000, 7000]
lista_cantidad = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#bienvenida


#Datos del cliente
nombre, apellido,dni,direccion,telefono,mail = datos_cliente()

#Creando lista de compra
matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)
mostrar_matriz(matriz)

lista_cantidad = lista_compras(lista_cantidad)

n = input("Desea seguir comprando?(Si/No)").capitalize()
while n == "Si":
    lista_cantidad = lista_compras(lista_cantidad)
    n = input("Desea seguir comprando?(Si/No)").capitalize()

total = sumador_total(lista_cantidad,lista_precios)

matriz = crear_matriz(lista_codigo,lista_articulos,lista_precios,lista_cantidad)
mostrar_compra(lista_cantidad,matriz)

#Envio
e = input("Quiere envio a domicilio(Si/No): ").capitalize()
if e == "Si":
    total = envio(total)
print(total)
    
#Factura

t_c = total_calzado(lista_cantidad)
t_a = total_accesorios(lista_cantidad)