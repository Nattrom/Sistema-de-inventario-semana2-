inventario = []

# Función para agregar productos

def agregar_producto():
    print("\n--- Agregar Producto ---")
    
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validación de precio
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except:
            print("Entrada inválida. Ingrese un número.")
    
    # Validación de cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except:
            print("Entrada inválida. Ingrese un número entero.")
    
    # Crear el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregar a la lista inventario
    inventario.append(producto)
    
    print("Producto agregado correctamente.\n")

# Función para mostrar el inventario

def mostrar_inventario():
    print("\n--- Inventario ---")
    
    # Verificar si está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.\n")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

# Función para calcular estadísticas

def calcular_estadisticas():
    print("\n--- Estadísticas ---")
    
    if len(inventario) == 0:
        print("No hay productos para calcular.\n")
        return
    
    total_valor = 0
    total_productos = 0
    
    # Recorrer el inventario
    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]
    
    print(f"Valor total del inventario: {total_valor}")
    print(f"Cantidad total de productos: {total_productos}\n")

# Menú principal con while

while True:
    print("=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    # Validación con condicionales
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.\n")
