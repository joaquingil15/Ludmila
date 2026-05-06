"""Trabajo practico Ludmila"""

"""funciones"""


"""VARIABLES"""

"""Factura"""

cant_factura = 0

"""prendas"""

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

sumador_accesorios = 0
max_accesorios = -9999

collares = 9000 
cont_collares = 0

anillos = 8000 
cont_anillos = 0

aros = 6000 
cont_aros = 0

pulseras = 7500 
cont_pulseras = 0




print("bienvenidos a Ludmila")
print("----------------------------------------------")

"""DATOS PERSONALES"""



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

for i in range(3):
    nombre = input("Ingrese su nombre y apellido: ").capitalize()
    dni = (input("Ingrese su DNI: "))
    envio = input("Ingrese su dirección: ")
    while len(dni) <= 7:
        dni = input("Ingrese un DNI válido")
    telefono = int(input("Ingrese su telefono: "))
    while len(telefono) <= 8 or len(telefono) <= 15:
        dni = input("Ingrese un numero de telefono válido")
    print("---------------------------------------------")
    print("Bienvenido", nombre)
    seguir = input("¿quiere empezar a comprar? ").upper()
    while seguir == "SI":
        opcion = input("ELIJA QUE QUIERE (PRENDAS/CALZADO/ACCESORIO): ").upper()

        if opcion == "PRENDAS":
            talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
            
            while talles != "S" and talles != "M" and talles != "L" and talles != "XL":
                print("ERROR - ELIGE ENTRE UN TALLE S/M/L/XL")
                talles = input("ELIJA UN TALLE S/M/L/XL: ").upper()
            
            prendas = input("ELIJA UNA PRENDA REMERAS/BUZOS/JEANS: ").upper()
            while prendas != "REMERAS" and prendas != "BUZOS" and prendas != "JEANS":
                print("ERROR")
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
            elif prendas == "JEANS":
                print("Jeans talle: ",talles)
                sumador_prendas = sumador_prendas + jeans
                cont_jeans = cont_jeans + 1
            
                if jeans > max_prendas:
                 max_prendas = jeans
            


        elif opcion == "CALZADO":
         eleccion_talles_calzado = int(input("ELIJA UN TALLE 36/37/38/40: "))

         while eleccion_talles_calzado != 36 and eleccion_talles_calzado != 37 and eleccion_talles_calzado != 38 and  eleccion_talles_calzado != 40:
            eleccion_talles_calzado = int(input("ERROR - ELIJA UN TALLE 36/37/38/40: "))

         eleccion_calzado = input("ELIJA UN TIPO DE CALZADO BOTAS TEXANAS/TACOS ").upper()
         while eleccion_calzado != "BOTAS TEXANAS" and eleccion_calzado != "TACOS":
            eleccion_calzado = input("ERROR - ELIJA UN CALZADO VÁLIDO BOTAS TEXANAS/TACOS: ").upper()
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
        elif opcion == "ACCESORIO":
          tipo_accesorio = input ("ELIJA UN ACCESORIO (COLLARES/ANILLOS/AROS/PULSERAS): ").upper()

          while tipo_accesorio != "COLLARES" and tipo_accesorio != "ANILLOS" and tipo_accesorio != "AROS" and tipo_accesorio != "PULSERAS":
            print ("ERROR - DEBE ELEGIR ACCESORIOS ENTRE COLLAR/ANILLO/AROS/PULSERAS")
            tipo_accesorio = input ("ELIJA UN ACCESORIO (COLLARES/ANILLOS/AROS/PULSERAS): ").upper()

          if tipo_accesorio == "COLLARES":
            sumador_accesorios = sumador_accesorios + collares
            cont_collares = cont_collares + 1 
            if collares > max_accesorios:
              max_accesorios = collares
          elif tipo_accesorio == "ANILLOS":
            sumador_accesorios = sumador_accesorios + anillos
            cont_anillos = cont_anillos + 1
            if anillos > max_accesorios:
              max_accesorios = anillos
          elif tipo_accesorio == "AROS":
            sumador_accesorios = sumador_accesorios + aros
            cont_aros = cont_aros + 1
            if aros > max_accesorios:
              max_accesorios = aros
          else:
            sumador_accesorios = sumador_accesorios + pulseras
            cont_pulseras = cont_pulseras + 1
            if pulseras > max_accesorios:
              max_accesorios = pulseras
        seguir = input("¿Desea seguir comprando? (SI/NO): ").upper()
    total = sumador_prendas + sumador_accesorios + sumador_calzado
    """envio"""
    print(""" Disponemos de envios a domicilio:
    CABA: $3000 / CONOURBANO: $4500 / INTERIOR: $6500""")
    envio = input("Quiere envio a domicilio: ").upper()
    if envio == "SI":
        localidad = input("Donde quiere que sea el envio: CABA/CONOURBANO/INTERIOR: ").upper()
        while localidad != "CABA" and localidad != "CONOURBANO" and localidad != "INTERIOR":
            localidad = input("Ingrese una localidad válida: ")
        if localidad == "CABA":
            total = total + 3000
        elif localidad == "CONOURBANO":
            total = total + 4500
        elif localidad == "INTERIOR":
            total = total + 6500
    

    """Factura"""

    cant_factura =+1

    total_calzado = cont_botas_texanas + cont_tacos

    total_accesorios = cont_collares + cont_anillos + cont_aros + cont_pulseras
    

    

    subtotal = total

    if total_accesorios > 0 and total_calzado > 0:

        subtotal = total*0.93 #descuento del 7%

    tipo_pago = input("Como desea abonar( Debito/Efectivo/Credito): ").lower()

    while tipo_pago != "debito" and tipo_pago != "efectivo" and tipo_pago != "credito":

        tipo_pago = input("Error - Como desea abonar( Debito/Efectivo/Credito): ").lower()

    if tipo_pago == "credito":

        cant_cuot = int(input("Numero de cuotas(Mas de 3 cuotas tiene recargo del 5%): "))

        while cant_cuot < 0 and cant_cuot > 24:

            cant_cuot = int(input("Error - Numero de cuotas(Mas de 3 cuotas tiene recargo del 5%): "))

        if cant_cuot > 3:

            subtotal = subtotal*1.05

            print("____________________________")

            print("Numero de factura",cant_factura)

            print("Dni:",dni)

            print("Numero de telefono:",telefono)

            print("Nombre del negocio: Ludmila")  

            print("Mail: ludmila@gmail.com") 

            print("Teléfono: 11 4875-8574")  

            print("CUIT: 30-68229475-7 ")

            print("____________________________")

            print("Total:",total)

            print("Subtotal:",subtotal)

            print("Subtotal:",subtotal,"Valor de cada cuota:",subtotal/cant_cuot)

            print("____________________________")
 
        else:

            print("____________________________")

            print("Numero de factura",cant_factura)

            print("Dni:",dni)

            print("Numero de telefono:",telefono)

            print("Nombre del negocio: Ludmila")

            print("Mail: ludmila@gmail.com") 

            print("Teléfono: 11 4875-8574")  

            print("CUIT: 30-68229475-7 ")

            print("____________________________")

            print("Total:",total)

            print("Subtotal:",subtotal)

            print("Subtotal:",subtotal,"Valor de cada cuota:",subtotal/cant_cuot)

            print("____________________________")

    else:

            print("____________________________")

            print("Numero de factura",cant_factura)

            print("Dni:",dni)

            print("Numero de telefono:",telefono)

            print("Nombre del negocio: Ludmila") 

            print("Mail: ludmila@gmail.com") 

            print("Teléfono: 11 4875-8574")  

            print("CUIT: 30-68229475-7 ")

            print("____________________________")

            print("Total:",total)

            print("Subtotal:",subtotal)

            print("____________________________")

 

    

        
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

"""CUENTAS ACCESORIOS"""
total_accesorios = cont_collares + cont_anillos + cont_aros + cont_pulseras
if total_accesorios > 0:
  promedio_accesorios = sumador_accesorios / total_accesorios
  porcentaje_collares = cont_collares * 100 / total_accesorios
  porcentaje_anillos = cont_anillos * 100 / total_accesorios
  porcentaje_aros = cont_aros * 100 / total_accesorios
  porcentaje_pulseras = cont_pulseras * 100 / total_accesorios
else: 
  promedio_accesorios = 0
  porcentaje_collares = 0
  porcentaje_anillos = 0
  porcentaje_aros = 0
  porcentaje_pulseras = 0


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

print("TOTAL A PAGAR POR LOS ACCESORIOS: $",sumador_accesorios)
print("ACCESORIO MÁS CARO: $",max_accesorios)
print("PROMEDIO GASTADO EN ACCESORIOS: ",promedio_accesorios)
print("PORCENTAJE DE COLLARES VENDIDOS: ",porcentaje_collares,"%")
print("PORCENTAJE DE ANILLOS VENDIDOS: ",porcentaje_anillos,"%")
print("PORCENTAJE DE AROS VENDIDOS: ",porcentaje_aros,"%")
print("PORCENTAJE DE PULSERAS VENDIDAS: ",porcentaje_pulseras,"%")
