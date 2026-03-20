#Todas las funciones hacen lo que su nombre dice

def agregar_producto (inventario): 
    nombre = input("\nIngresa el nombre del producto: ") 
    for producto in inventario: #Ciclo for que recorre cada producto del inventario
        if producto["nombre"] == nombre: #Esto es para verificar si el producto que se va a ingresar ya esta en el inventario
            cantidad = int(input("Ingresa la cantidad que vas a llevar: ")) #Variable que guarda la cantidad de producto
            producto ["cantidad"] += cantidad #Aca se suma la cantidad nueva con la anterior registrada
            return
        
    intentos_bucle = 0 #Cantidad de veces que se ha intentado ingresar un dato y ha sucedido algun error
    while True: 
        if intentos_bucle == 3: #Si ya van 3 veces que el usuario ha tenido un error lo saca del bucle 
            print("Error, numero maximo de intentos alcanzado")
            return 
        try:
             precio = int(input("Ingresa el precio del producto: ")) 
             if precio < 0: #Aca mira si el precio ingresado es negativo, si es negativo lo cuenta como error
                 print("Por favor ingresa un numero mayor que 0")
                 intentos_bucle += 1 
                 continue
             break #Si el dato ingresado es positivo y efectivamente es un numero se sale del ciclo while
        except ValueError: #Excepcion por si ingresa algo diferente a un numero
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1
    
    intentos_bucle = 0
    #Esto ciclo while hace lo mismo que el ciclo de arriba, lo unico diferente es el inventario.append
    while True:
        if intentos_bucle == 3:
            print("Error, numero maximo de intentos alzancado")
            return
        try:
            cantidad = int(input("Ingresa la cantidad que vas a llevar: "))
            if cantidad < 0:
                print("Por favor ingresa un numero mayor que 0")
                intentos_bucle += 1
                continue
            inventario.append({"nombre":nombre,"precio":precio,"cantidad":cantidad}) #Si no hay ningun error se ingresa el producto en el inventario
            break
        except ValueError:
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1
    
def mostrar_inventario (inventario):
    if len(inventario) != 0: #Esto valida que haya tansiquiera 1 producto
        for producto in inventario: #Ciclo que recorre cada uno de los productos en el inventario
            print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | cantidad: {producto["cantidad"]}") #Y pues aja aca imprime los productos
    else: #Si no hay ningun producto imprime lo de abajo
        print("No hay nada registrado aun")

def calcular_estadisticas(inventario):
    valor_total_inventario = 0 
    total_productos_registrados = len(inventario) #Variable que almacena la cantidad de productos registrados
    for producto in inventario:
        valor_total_producto = producto["precio"] * producto["cantidad"] #Esto es una variable que calcula el valor total de cada producto
        valor_total_inventario += valor_total_producto #Aca simplemente se suma el valor total del inventario con el valor total de cada producto
    print(f"Productos registrados : {total_productos_registrados} | valor total del inventario: ${valor_total_inventario}")