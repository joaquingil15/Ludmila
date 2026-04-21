"""Trabajo practico Ludmila"""

"""VARIABLES"""

"""prendas"""
seguir = "SI"
sumador_prendas = 0
max_prendas = -9999
remeras = 15000
cont_remeras = 0

buzos = 20000 
cont_buzos = 0

jeans = 30000
cont_jeans = 0

"""calzado"""
botas_texanas =45000 

tacos = 35000

"""accesorios"""

collares = 9000 

anillos = 8000 

aros =6000 

pulseras =7500 



print("bienvenidos a Ludmila")
print("----------------------------------------------")

"""DATOS PERSONALES"""

nombre = input("Ingrese su nombre y apellido: ").capitalize()
dni = int(input("Ingrese su DNI: "))
telefono = int(input("Ingrese su telefono: "))

print("""NUESTROS PRODUCTOS
TALLES: S (pequeño), M (Mediano), L (Grande) y XL (Extra Grande) 

-Remeras $15000 

-Buzos $20000 

-Jeans $30000  

TALLES CALZADO: 36, 37, 38 y 40 

-Botas texanas $45000 

-Tacos $35000 

ACCESORIOS: 

-Collares $9000 

-Anillos $8000 

-Aros $6000 

-Pulseras $7500 

Posibilidad de descuento y cuánto: 7% descuento si se lleva un calzado y un accesorio.  

Posibilidad de recargo y cuánto: 5% más de 3 cuotas. 

""")

print("---------------------------------------------")

while seguir == "SI":
    opcion = input("ELIJA QUE QUIERE (PRENDAS/CALZADO/ACCESORIO): ").capitalize()

    if opcion == "Prendas":
        talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
        
        while talles != "S" and talles != "M" and talles != "L" and talles != "XL":
            print("ERROR - ELIGE ENTRE UN TALLE S/M/L/XL")
            talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
        
        prendas = input("ELIJA UNA PRENDA REMERAS/BUZOS/JEANS: ").capitalize()
        if prendas == "Remeras":
            print("Remera talle: ",talles)
            sumador_prendas = sumador_prendas + remeras
            cont_remeras = cont_remeras + 1
        elif prendas == "Buzos":
            print("Buzos talle: ",talles)
            sumador_prendas = sumador_prendas + buzos
            cont_buzos = cont_buzos + 1
        else:
            print("Jeans talle: ",talles)
            sumador_prendas = sumador_prendas + jeans
            cont_jeans = cont_jeans + 1
        if sumador_prendas>max_prendas: #ESTA MAL EL MAXIMO
            max_prendas = sumador_prendas
        seguir = input("¿Desea seguir comprando? (SI/NO): ").upper()
        

"""impresión PRENDAS"""
total_prendas = cont_remeras + cont_buzos + cont_jeans
prom_prendas = sumador_prendas/total_prendas
por_remeras = cont_remeras*100/total_prendas
por_buzos = cont_buzos*100/total_prendas
por_jeans = cont_jeans*100/total_prendas
print("TOTAL A PAGAR POR LAS PRENDAS $",sumador_prendas)
print("PRENDA MAS CARA $",max_prendas)
print("PORCENTAJE DE PRENDAS VENDIDAS: ",prom_prendas,"%")
print("PROMEDIO DE REMERAS VENDIDAS: ",por_remeras,"%")
print("PROMEDIO DE BUZOS VENDIDAS: ",por_buzos,"%")
print("PROMEDIO DE JEANS VENDIDAS: ",por_jeans,"%")




