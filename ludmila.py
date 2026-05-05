"""Trabajo practico Ludmila"""

"""funciones"""


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

max_calzado = 0
sumador_calzado = 0

botas_texanas =45000 
cont_botas_texanas = 0

tacos = 35000
cont_tacos = 0

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
    opcion = input("ELIJA QUE QUIERE (PRENDAS/CALZADO/ACCESORIO): ").upper()

    if opcion == "PRENDAS":
        talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
        
        while talles != "S" and talles != "M" and talles != "L" and talles != "XL":
            print("ERROR - ELIGE ENTRE UN TALLE S/M/L/XL")
            talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
        
        prendas = input("ELIJA UNA PRENDA REMERAS/BUZOS/JEANS: ").upper()
        if prendas == "REMERAS":
            print("Remera talle: ",talles)
            sumador_prendas = sumador_prendas + remeras
            cont_remeras = cont_remeras + 1
            if remeras > max_prendas:
             max_prendas = remeras
        elif prendas == "BUZOS":
            print("Buzos talle: ",talles)
            sumador_prendas = sumador_prendas + buzos
            cont_buzos = cont_buzos + 1
            if buzos > max_prendas:
             max_prendas = buzos
        else:
            print("Jeans talle: ",talles)
            sumador_prendas = sumador_prendas + jeans
            cont_jeans = cont_jeans + 1
            if jeans > max_prendas:
             max_prendas = jeans


    elif opcion == "CALZADO":
     eleccion_talles_calzado = int(input("ELIJA UN TALLE 36/37/38/40"))

     while eleccion_talles_calzado != 36 and eleccion_talles_calzado != 37 and eleccion_talles_calzado != 38 and  eleccion_talles_calzado != 40:
        print("ERROR - ELIGE ENTRE UN TALLE 36/37/38/40")
        eleccion_talles_calzado = int(input("ELIJA UN TALLE 36/37/38/40: "))

     eleccion_calzado = input("ELIJA UN TIPO DE CALZADO BOTAS TEXANAS/TACOS ").upper()
     if eleccion_calzado == "BOTAS TEXANAS":
        print("BOTAS TEXANAS TALLE: ",eleccion_talles_calzado)
        sumador_calzado = sumador_calzado + botas_texanas
        cont_botas_texanas = cont_botas_texanas + 1
        if botas_texanas > max_calzado:
           max_calzado = botas_texanas
     elif eleccion_calzado == "TACOS":
        print("TACOS: ",eleccion_talles_calzado)
        sumador_calzado = sumador_calzado + tacos
        cont_tacos = cont_tacos + 1
        if tacos > max_calzado:
             max_calzado = tacos 
    seguir = input("¿Desea seguir comprando? (SI/NO): ").upper()

        

"""CUENTAS PRENDAS"""
total_prendas = cont_remeras + cont_buzos + cont_jeans
if total_prendas > 0:
    prom_prendas = sumador_prendas / total_prendas
    por_remeras = cont_remeras * 100 / total_prendas
    por_buzos = cont_buzos * 100 / total_prendas
    por_jeans = cont_jeans * 100 / total_prendas
else:
     prom_prendas = 0
     por_remeras = 0
     por_buzos = 0
     por_jeans = 0

"""CUENTAS CALZADO"""
total_calzado = cont_botas_texanas + cont_tacos
if total_calzado > 0:
    prom_calzado = sumador_calzado / total_calzado
    por_botas_texanas = cont_botas_texanas * 100 / total_calzado
    por_tacos = cont_tacos * 100 / total_calzado
else:
    prom_calzado = 0
    por_botas_texanas = 0
    por_tacos = 0





print("TOTAL A PAGAR POR LAS PRENDAS $",sumador_prendas)
print("PRENDA MAS CARA $",max_prendas)
print("PORCENTAJE DE PRENDAS VENDIDAS: ",prom_prendas,"%")
print("PROMEDIO DE REMERAS VENDIDAS: ",por_remeras,"%")
print("PROMEDIO DE BUZOS VENDIDAS: ",por_buzos,"%")
print("PROMEDIO DE JEANS VENDIDAS: ",por_jeans,"%")

print("TOTAL A PAGAR POR EL CALZADO $", sumador_calzado)
print("CALZADO MAS CARO $", max_calzado)
print("PROMEDIO GASTADO EN CALZADO: $", prom_calzado)
print("PORCENTAJE DE BOTAS TEXANAS VENDIDAS: ", por_botas_texanas, "%")
print("PORCENTAJE DE TACOS VENDIDOS: ", por_tacos, "%")



