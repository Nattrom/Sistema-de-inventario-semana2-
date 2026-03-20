# 📦 Sistema de Inventario en Python
🧾 Descripción

Este proyecto consiste en un sistema básico de inventario desarrollado en Python.
Permite al usuario gestionar productos mediante un menú interactivo en consola.

El sistema incluye funcionalidades para agregar productos, visualizar el inventario y calcular estadísticas.

🎯 Objetivo

Aplicar conceptos fundamentales de programación como:

Listas

Diccionarios

Condicionales (if, elif, else)

Ciclos (while, for)

Funciones

Validación de datos

⚙️ Funcionalidades
1. Agregar producto

Permite ingresar:

Nombre del producto

Precio

Cantidad

Cada producto se almacena como un diccionario dentro de una lista llamada inventario.

Ejemplo:

producto = {"nombre": "Lápiz", "precio": 500, "cantidad": 3}
2. Mostrar inventario

Muestra todos los productos registrados.

Si no hay productos, indica que el inventario está vacío.

Formato de salida:

Producto: Lápiz | Precio: 500 | Cantidad: 3
3. Calcular estadísticas

Calcula:

Valor total del inventario (precio × cantidad)

Cantidad total de productos

4. Menú interactivo

El sistema muestra un menú que permite elegir opciones:

1. Agregar producto
2. Mostrar inventario
3. Calcular estadísticas
4. Salir

Se ejecuta continuamente usando un ciclo while

Maneja errores si el usuario ingresa opciones inválidas

🧠 Estructura del código

El programa está organizado en funciones:

agregar_producto() → Registra productos

mostrar_inventario() → Muestra los datos

calcular_estadisticas() → Realiza cálculos

while principal → Controla el menú

🔒 Validaciones

Evita ingresar valores negativos

Controla errores de tipo (texto en lugar de números)

No permite que el programa se cierre por entradas incorrectas

🚀 Cómo ejecutar

Abrir Visual Studio Code o cualquier editor

Crear un archivo .py

Copiar el código

Ejecutar en la terminal:

python nombre_del_archivo.py
🧩 Tecnologías usadas

Python (nivel básico)

📌 Conclusión

Este programa permite gestionar un inventario de forma sencilla desde consola.
Se aplican buenas prácticas como modularización del código, validación de datos y uso de estructuras fundamentales de programación.
