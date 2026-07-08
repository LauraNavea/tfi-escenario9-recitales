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
def ejecutar_sistema():
    # 1. INICIALIZACIÓN
    c_vip, v_vip, p_vip = 500, 0, 250000
    c_gral, v_gral, p_gral = 5000, 0, 150000
    c_pref, v_pref, p_pref = 1500, 0, 180000
    c_baj, v_baj, p_baj = 2500, 0, 130000
    c_alt, v_alt, p_alt = 3000, 0, 100000
    c_pop, v_pop, p_pop = 5000, 0, 70000
    total_recaudado = 0
    total_entradas = 0
    
    # FUNCIONES INTERNAS (Tienen acceso directo a las variables de arriba)
    def calcular_sector_mas_demandado():
        mayor = v_vip
        sector = "Campo VIP"
        if v_gral > mayor: mayor = v_gral; sector = "Campo General"
        if v_pref > mayor: mayor = v_pref; sector = "Platea Preferencial"
        if v_baj > mayor: mayor = v_baj; sector = "Platea Baja"
        if v_alt > mayor: mayor = v_alt; sector = "Platea Alta"
        if v_pop > mayor: mayor = v_pop; sector = "Popular"
        return sector

    def mostrar_estadisticas():
        print("\n--- ESTADÍSTICAS FINALES ---")
        print(f"VIP: {v_vip} | Gral: {v_gral} | Pref: {v_pref}")
        print(f"Baja: {v_baj} | Alta: {v_alt} | Pop: {v_pop}")
        print(f"Recaudado: ${total_recaudado:,.0f}")
        print("Sector más demandado:", calcular_sector_mas_demandado())

    # 3. BUCLE PRINCIPAL
    while True:
        print("\n--- SELECCIONE SECTOR ---")
        print(f"1. VIP (Disp: {c_vip - v_vip}) | 2. Gral (Disp: {c_gral - v_gral})")
        print(f"3. Pref (Disp: {c_pref - v_pref}) | 4. Baja (Disp: {c_baj - v_baj})")
        print(f"5. Alta (Disp: {c_alt - v_alt}) | 6. Pop (Disp: {c_pop - v_pop})")
        
        opc_s = input("Opción: ").strip()
        precio_base = 0
        if opc_s == "1" and v_vip < c_vip: v_vip += 1; precio_base = p_vip
        elif opc_s == "2" and v_gral < c_gral: v_gral += 1; precio_base = p_gral
        elif opc_s == "3" and v_pref < c_pref: v_pref += 1; precio_base = p_pref
        elif opc_s == "4" and v_baj < c_baj: v_baj += 1; precio_base = p_baj
        elif opc_s == "5" and v_alt < c_alt: v_alt += 1; precio_base = p_alt
        elif opc_s == "6" and v_pop < c_pop: v_pop += 1; precio_base = p_pop
        else: print("¡Error!"); continue
            
        desc = input("Descuento (1.Antic, 2.Prev, 3.Pack, 4.Nada): ").strip()
        tasa = 0.35 if desc=="1" else 0.15 if desc=="2" else 0.23 if desc=="3" else 0
        precio_final = precio_base * (1 - tasa)
        total_recaudado += precio_final
        total_entradas += 1
        
        if input("¿Salir? (s/n): ").strip() == 's': break
            
    # 4. LLAMADA AL FINAL
    mostrar_estadisticas()
    input("\nPresiona Enter para cerrar...")

if __name__ == "__main__":
    ejecutar_sistema()