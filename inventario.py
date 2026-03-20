inventario = []
salir_bucle = 0
def agregar_producto ():
    nombre = input("\nIngresa el nombre del producto: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            cantidad = int(input("Ingresa la cantidad que vas a llevar: "))
            producto ["cantidad"] += cantidad
            return
        
    intentos_bucle = 0
    while True:
        if intentos_bucle == 3:
            print("Error, numero maximo de intentos alcanzado")
            return
        try:
             precio = int(input("Ingresa el precio del producto: "))
             if precio < 0:
                 print("Por favor ingresa un numero mayor que 0")
                 intentos_bucle += 1
                 continue
             break
        except ValueError:
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1
    
    intentos_bucle = 0
    while True:
        if intentos_bucle == 3:
            print("Error, numero maximo de intentos alzancado")
            return
        try:
            cantidad = int(input("Ingresal la cantidad que vas a llevar: "))
            if cantidad < 0:
                print("Por favor ingresa un numero mayor que 0")
                intentos_bucle += 1
                continue
            inventario.append({"nombre":nombre,"precio":precio,"cantidad":cantidad})
            break
        except ValueError:
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1

def mostrar_inventario ():
    if len(inventario) != 0:
        for producto in inventario:
            print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | cantidad: {producto["cantidad"]}")
    else:
        print("No hay nada registrado aun")

def calcular_estadisticas():
    valor_total_inventario = 0
    total_productos_registrados = len(inventario)
    for producto in inventario:
        valor_total_producto = producto["precio"] * producto["cantidad"]
        valor_total_inventario += valor_total_producto
    print(f"Productos registrados : {total_productos_registrados} | valor total del inventario: ${valor_total_inventario}")

while salir_bucle == 0:
    print("""
Hola, que quieres hacer?

1. Agregar Producto
2. Mostrar inventario
3. Calcular Estadisticas
4. Salir
          """)
    opcion = input("Escoge una opcion: ")

    if opcion == "1":
        seguir_agregando = "si"
        while seguir_agregando != "no":
            agregar_producto()
            seguir_agregando = input("Quieres agregar otro producto? si/no: ")
    elif opcion == "2":
        print("\nInventario")
        mostrar_inventario()
    elif opcion == "3":
        print("\nEstadisticas")
        calcular_estadisticas()
    elif opcion == "4":
        print("Chao")
        salir_bucle = 1
    else:
        print("Ingresa una opcion valida")