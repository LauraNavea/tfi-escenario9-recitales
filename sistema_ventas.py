```python
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
            print("\n[Módulo de registro en desarrollo...]")
        elif opcion_menu == 2:
            print("\nFinalizando la jornada de operaciones...")
        else:
            print("Error: Opción incorrecta. Marque 1 o 2.")

if __name__ == "__main__":
    main()