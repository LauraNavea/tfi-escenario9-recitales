# Capacidad máxima por cada sector
cap_vip = 500
cap_gral = 2000
cap_pref = 1200
cap_alt = 1500
cap_baj = 1800
cap_pop = 3000
 
# Contadores para el total de entradas vendidas y dinero
cont_vip = 0
cont_gral = 0
cont_pref = 0
cont_alt = 0
cont_baj = 0
cont_pop = 0
acum_dinero_total = 0.0
 
archivo_nombre = "registro_ventas.txt"
 
def validar_fecha(dia, mes, anio):
    """
    Valida que el día, mes y año ingresados sean correctos.
    """
    if anio < 2026:
        return False
    if not (1 <= mes <= 12):
        return False
    
    # Ver si el año es bisiesto para los días de febrero
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    # Guardar la cantidad de días máximos que tiene el mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    elif mes == 2:
        max_dias = 29 if es_bisiesto else 28
    else:
        return False
        
    return 1 <= dia <= max_dias
 
def procesar_sector(sector, cantidad):
    """
    Revisa si hay lugar, resta las entradas, suma a los contadores
    y devuelve el precio base de ese sector. Si no alcanza, devuelve 0.0.
    """
    global cap_vip, cap_gral, cap_pref, cap_alt, cap_baj, cap_pop
    global cont_vip, cont_gral, cont_pref, cont_alt, cont_baj, cont_pop
    
    precio_base = 0.0
 
    if sector == "Campo_VIP":
        if cap_vip >= cantidad:
            cap_vip -= cantidad
            cont_vip += cantidad
            precio_base = 150000.0
            
    elif sector == "General":
        if cap_gral >= cantidad:
            cap_gral -= cantidad
            cont_gral += cantidad
            precio_base = 45000.0
            
    elif sector == "Platea_Preferencial":
        if cap_pref >= cantidad:
            cap_pref -= cantidad
            cont_pref += cantidad
            precio_base = 95000.0
            
    elif sector == "Platea_Alta":
        if cap_alt >= cantidad:
            cap_alt -= cantidad
            cont_alt += cantidad
            precio_base = 60000.0
            
    elif sector == "Platea_Baja":
        if cap_baj >= cantidad:
            cap_baj -= cantidad
            cont_baj += cantidad
            precio_base = 75000.0
            
    elif sector == "Popular":
        if cap_pop >= cantidad:
            cap_pop -= cantidad
            cont_pop += cantidad
            precio_base = 30000.0
 
    return precio_base
 
def calcular_sector_mas_demandado():
    """
    Busca cuál de todos los sectores vendió más entradas y devuelve su nombre.
    """
    mayor = cont_vip
    sector = "Campo_VIP"
 
    if cont_gral > mayor:
        mayor = cont_gral
        sector = "General"
 
    if cont_pref > mayor:
        mayor = cont_pref
        sector = "Platea_Preferencial"
 
    if cont_alt > mayor:
        mayor = cont_alt
        sector = "Platea_Alta"
 
    if cont_baj > mayor:
        mayor = cont_baj
        sector = "Platea_Baja"
 
    if cont_pop > mayor:
        mayor = cont_pop
        sector = "Popular"
 
    return sector
 
def mostrar_estadisticas():
    """
    Muestra por pantalla los totales de ventas y el sector más vendido.
    """
    print("==================================================")
    print("            ESTADÍSTICAS FINALES DE VENTAS       ")
    print("==================================================")
    print("Entradas vendidas por sector:")
    print(f" - Campo VIP: {cont_vip}")
    print(f" - General: {cont_gral}")
    print(f" - Platea Preferencial: {cont_pref}")
    print(f" - Platea Alta: {cont_alt}")
    print(f" - Platea Baja: {cont_baj}")
    print(f" - Popular: {cont_pop}")
    print("--------------------------------------------------")
    print(f"Monto total de dinero acumulado: ${acum_dinero_total:.2f}")
    print("----------------------------------------------")
    print("Sector más demandado:", calcular_sector_mas_demandado())
    print("==================================================")
 
# --- PROGRAMA PRINCIPAL ---
def main():
    global acum_dinero_total
    opcion_menu = 0
 
    # Variables para guardar los datos de la venta actual
    nombre_recital = ""
    v_dia = 0
    v_mes = 0
    v_anio = 0
    v_sector = ""
    v_cantidad = 0
    v_descuento = ""
    v_total_pago = 0.0
 
    while opcion_menu != 2:
        print("\n--- SISTEMA DE VENTA DE ENTRADAS PARA RECITALES ---")
        print("1. Registrar una nueva venta")
        print("2. Salir y cerrar caja")
        
        try:
            opcion_menu = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            continue
 
        if opcion_menu == 1:
            # Pedir los datos de la venta
            nombre_recital = input("Ingrese el nombre del recital: ")
 
            # Pedir la fecha y validar que sea correcta
            while True:
                try:
                    v_dia = int(input("Ingrese el día del evento: "))
                    v_mes = int(input("Ingrese el número de mes (1-12): "))
                    v_anio = int(input("Ingrese el año (2026 en adelante): "))
                    
                    # Llamar a la función para verificar la fecha
                    if validar_fecha(v_dia, v_mes, v_anio):
                        break
                    else:
                        print("Error: La fecha ingresada es inválida o inexistente. Intente nuevamente.")
                except ValueError:
                    print("Error: Los datos de la fecha deben ser números enteros.")
 
            # Pedir el sector y controlar que sea una opción válida
            while True:
                v_sector = input("Seleccione el sector (Campo_VIP, General, Platea_Preferencial, Platea_Alta, Platea_Baja, Popular): ")
                if v_sector in ["Campo_VIP", "General", "Platea_Preferencial", "Platea_Alta", "Platea_Baja", "Popular"]:
                    break
                print("Error: El nombre del sector no coincide con las opciones vigentes.")
 
            # Pedir la cantidad de entradas
            while True:
                try:
                    v_cantidad = int(input("Ingrese la cantidad de entradas a comprar (mínimo 1): "))
                    if v_cantidad > 0:
                        break
                    print("Error: La cantidad debe ser mayor a cero.")
                except ValueError:
                    print("Error: Ingrese un número entero.")
 
            # Pedir el tipo de descuento
            while True:
                v_descuento = input("Ingrese el tipo de descuento (anticipado, preventa, pack, ninguno): ")
                if v_descuento in ["anticipado", "preventa", "pack", "ninguno"]:
                    break
                print("Error: Tipo de descuento no válido.")
 
            # Verificar disponibilidad del sector
            precio_base = procesar_sector(v_sector, v_cantidad)
 
            if precio_base > 0.0:
                # Aplicar el descuento correspondiente al precio base
                if v_descuento == "anticipado":
                    precio_final = precio_base * 0.80
                elif v_descuento == "preventa":
                    precio_final = precio_base * 0.90
                elif v_descuento == "pack":
                    precio_final = precio_base * 0.85
                else:
                    precio_final = precio_base
 
                v_total_pago = precio_final * v_cantidad
                acum_dinero_total += v_total_pago
 
                print("¡Venta procesada con éxito!")
                print(f"Monto total a abonar por esta operación: ${v_total_pago:.2f}")
 
                # Guardar los datos en el archivo de texto (Cambio aplicado aquí)
                with open(archivo_nombre, "a") as f:
                    f.write(f"{nombre_recital};"
                            f"{v_dia};"
                            f"{v_mes};"
                            f"{v_anio};"
                            f"{v_sector};"
                            f"{v_cantidad};"
                            f"{v_descuento};"
                            f"{v_total_pago:.2f}\n")
            else:
                print(f"Error: No hay lugares disponibles suficientes en {v_sector}.")
 
        elif opcion_menu == 2:
            print("\nFinalizando la jornada de operaciones...")
        else:
            print("Error: Opción incorrecta. Marque 1 o 2.")
 
    # Mostrar estadísticas y cerrar el programa
    mostrar_estadisticas()
    print(f"Datos guardados en el archivo de texto '{archivo_nombre}'")
    print("Programa finalizado correctamente.")
 
if __name__ == "__main__":
    main()
