import os
print(os.getcwd()) #imprime por pantalla la direccion donde se creo el archivo.txt
# =====================================================================
# VARIABLES GLOBALES - Control de Inventario (Capacidad máxima)
# =====================================================================
cap_vip = 500
cap_gral = 2000
cap_pref = 1200
cap_alt = 1500
cap_baj = 1800
cap_pop = 3000
 
# Contadores acumulativos para registrar entradas vendidas por sector
cont_vip = 0
cont_gral = 0
cont_pref = 0
cont_alt = 0
cont_baj = 0
cont_pop = 0

# Acumulador monetario total del día
acum_dinero_total = 0.0
 
# Nombre del archivo físico secuencial donde se guardarán los datos
archivo_nombre = "registro_ventas.txt"

# Validacion de Fecha para que el usuario ingrese una fecha valida
def validar_fecha(dia, mes, anio):
    if anio < 2026:
        return False
    if not (1 <= mes <= 12):
        return False
    
    # Algoritmo matemático para determinar bisiesto sin usar librerías externas
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    elif mes == 2:
        max_dias = 29 if es_bisiesto else 28
    else:
        return False
        
    return 1 <= dia <= max_dias

# =====================================================================
# FUNCIÓN PRINCIPAL DEL SISTEMA
# =====================================================================
def main():
    global acum_dinero_total
    opcion_menu = 0
 
    # Ciclo de control interactivo (Menú)
    while opcion_menu != 2:
        print("\n--- SISTEMA DE VENTA DE ENTRADAS PARA RECITALES ---")
        print("1. Registrar una nueva venta")
        print("2. Salir y cerrar caja")
        
        try:
            opcion_menu = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido (1 o 2).")
            continue

        if opcion_menu == 1:
            nombre_recital = input("Ingrese el nombre del recital: ")
 
            while True:
                try:
                    v_dia = int(input("Ingrese el día del evento: "))
                    v_mes = int(input("Ingrese el número de mes (1-12): "))
                    v_anio = int(input("Ingrese el año (2026 en adelante): "))
                    
                    if validar_fecha(v_dia, v_mes, v_anio):
                        break
                    else:
                        print("Error: La fecha ingresada es inválida o inexistente. Intente nuevamente.")
                except ValueError:
                    print("Error: Los datos de la fecha deben ser números enteros.")
        elif opcion_menu == 2:
            print("\nFinalizando la jornada de operaciones...")
        else:
            print("Error: Opción incorrecta. Marque 1 o 2.")

if __name__ == "__main__":
    main()