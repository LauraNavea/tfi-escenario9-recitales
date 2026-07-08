# Trabajo Final Integrador: Sistema de Venta de Entradas para Recitales

## 👥 Integrantes del Grupo

- **Ferreyra, Juan Manuel** — Legajo:
- **Gómez Parodi, Estanislao** — Legajo:
- **Navea Villasmil, Laura Isabel** — Legajo: **27864**
- **Robles, Francisco Leonel** — Legajo: **29903**

---

## 🏫 Comisión

- **Carrera:** Ingeniería en Sistemas de Información (UTN FRRE)
- **Comisión:** ISI D (1.4)
- **Asignatura:** Algoritmos y Estructuras de Datos

---

## 📝 Descripción General del Sistema

Este programa en Python administra la venta y reserva de entradas para recitales masivos (**Escenario 9**).

El sistema permite:

- Controlar en tiempo real la capacidad disponible de **6 sectores**:
  - Campo VIP
  - Campo General
  - Platea Preferencial
  - Platea Alta
  - Platea Baja
  - Popular
- Calcular automáticamente el importe de cada operación aplicando una **matriz de descuentos**:
  - Compra anticipada
  - Preventa
  - Pack de entradas
- Registrar de forma secuencial todas las operaciones en un archivo físico `.txt`.
- Generar al finalizar la jornada un resumen estadístico con:
  - Total de entradas vendidas por sector.
  - Recaudación total.
  - Sector con mayor demanda.

---

## 🚀 Instrucciones de Ejecución

1. Tener instalado **Python 3.10** o superior.
2. Descargar el archivo `sistema_ventas.py`.
3. Abrir una terminal dentro de la carpeta donde se encuentra el archivo.
4. Ejecutar el siguiente comando:

```
python sistema_ventas.py
```

---

# 🧠 Registro de Uso Crítico de Inteligencia Artificial (IA)

## 1. ¿Qué IA utilizamos y para qué?

**ChatGPT** fue utilizado como un asistente de consulta técnica para resolver dudas específicas y ayudar en la depuración de errores puntuales.

### Consultas realizadas

- **Sintaxis de Python**
  - Apertura de archivos en modo de anexado mediante `with open(..., "a")`.
  - Formateo de números flotantes para mostrar dos decimales (`:.2f`).

- **Manejo de excepciones**
  - Ejemplos prácticos del uso de bloques `try-except`.
  - Captura del error `ValueError` cuando el usuario ingresa texto en lugar de números enteros.

---

## 2. ¿Cómo y por qué validamos los resultados? (Control Crítico)

### Verificación de la lógica

Las respuestas generadas por la IA fueron analizadas y adaptadas por el equipo.

En varias oportunidades la IA propuso soluciones utilizando funciones avanzadas o librerías que aún no habían sido vistas en la materia. Dichas propuestas fueron descartadas y reemplazadas por implementaciones desarrolladas únicamente con los contenidos trabajados en la cátedra, utilizando:

- Estructuras condicionales (`if`, `elif`, `else`).
- Estructuras repetitivas (`while`).
- Funciones propias.
- Operadores matemáticos básicos.
- Validaciones realizadas manualmente.

De esta manera, el programa cumple con el nivel de conocimientos requerido para la asignatura.

### Pruebas realizadas

Cada sugerencia obtenida fue verificada ejecutando el programa manualmente desde la consola.

Se realizaron pruebas sobre diferentes situaciones, entre ellas:

- Ingreso de datos inválidos.
- Errores de stock o capacidad.
- Fechas incorrectas.
- Cálculo de descuentos.
- Registro de operaciones en el archivo.

Esto permitió comprobar que las validaciones implementadas por el grupo funcionaban correctamente y que el funcionamiento del sistema no dependía de aceptar automáticamente las respuestas proporcionadas por la IA.
