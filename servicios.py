def agregar_producto (inventario):
    """
    Agrega un diccionario con la siguiente estructura: {"nombre":nombre,"precio":precio,"cantidad":cantidad}, esto se guarda en la lista inventario

    parametros:
    Inventario

    retorna:
    Nada
    """
    se_guardo = False
    intentos_bucle = 0
    while se_guardo == False:
        if intentos_bucle == 3:
            print("\nError, numero maximo de intentos alcanzado")
            return
        nombre = input("\nIngresa el nombre del producto: ").strip() 
        if len(nombre) == 0: #Si no se ingreso nada, lo cuenta como error y vuelve a pedir el nombre
            print("El nombre no puede estar vacio")
            intentos_bucle +=1
            continue
        else:
            for producto in inventario: #Ciclo for que recorre cada producto del inventario
                if producto["nombre"] == nombre: #Esto es para verificar si el producto que se va a ingresar ya esta en el inventario
                    cantidad = int(input("Ingresa la cantidad que vas a llevar: ")) #Variable que guarda la cantidad de producto
                    producto ["cantidad"] += cantidad #Aca se suma la cantidad nueva con la anterior registrada
                    return
        se_guardo = True
        
    intentos_bucle = 0 #Cantidad de veces que se ha intentado ingresar un dato y ha sucedido algun error
    se_guardo = False
    while se_guardo == False: 
        if intentos_bucle == 3: #Si ya van 3 veces que el usuario ha tenido un error lo saca del bucle 
            print("Error, numero maximo de intentos alcanzado")
            return 
        try:
             precio = float(input("Ingresa el precio del producto: ")) 
             if precio < 0: #Aca mira si el precio ingresado es negativo, si es negativo lo cuenta como error
                 print("Por favor ingresa un numero mayor que 0")
                 intentos_bucle += 1 
                 continue
             se_guardo = True #Si el dato ingresado es positivo y efectivamente es un numero se sale del ciclo while
        except ValueError: #Excepcion por si ingresa algo diferente a un numero
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1
    
    intentos_bucle = 0
    #Esto ciclo while hace lo mismo que el ciclo de arriba, lo unico diferente es el inventario.append
    se_guardo = False
    while se_guardo == False:
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
            se_guardo = True
        except ValueError:
            print("Por favor ingresa una cantidad valida\n")
            intentos_bucle += 1
    
def mostrar_inventario (inventario):
    """
    Muestra la lista inventario, ahi estan todos los productos registrados hasta el momento

    parametros:
    Inventario

    retorna:
    Nada
    """
    if len(inventario) != 0: #Esto valida que haya tansiquiera 1 producto
        for producto in inventario: #Ciclo que recorre cada uno de los productos en el inventario
            print(f"Producto: {producto["nombre"]} | Precio: ${producto["precio"]} | cantidad: {producto["cantidad"]}") #Y pues aja aca imprime los productos
    else:
        print("No hay nada registrado aun")

def calcular_estadisticas(inventario):
    """
    Calcula las estadisticas del inventario calculando el subtotal de cada producto y sumandolos para dar un total general,
      tambien la cantidad de productos que hay registrados y cual es el mas caro y cual tiene mayor stock

    Parametros:
    Inventario

    Retorna:
    Nada
    """
    if len(inventario) > 0:
        valor_total_inventario = 0 
        cantidad_productos_registrados = len(inventario) 
        producto_mas_caro = inventario[0] #aca se pone por defecto el primer producto
        producto_mas_stock = inventario[0] #aca lo mismo
    else:
        print("No hay nada registrado todavia")
        return
    for producto in inventario:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        if producto["cantidad"] > producto_mas_stock["cantidad"]:
            producto_mas_stock = producto

        valor_total_producto = producto["precio"] * producto["cantidad"] #Esto es una variable que calcula el valor total de cada producto
        valor_total_inventario += valor_total_producto #Aca simplemente se suma el valor total del inventario con el valor total de cada producto
    print(f"Productos registrados : {cantidad_productos_registrados} | valor total del inventario: ${valor_total_inventario} | producto mas caro: {producto_mas_caro["nombre"]}, precio: {producto_mas_caro["precio"]} | producto con mas stock: {producto_mas_stock["nombre"]}, cantidad: {producto_mas_stock["cantidad"]}")

def buscar_producto(inventario):
  """
  Busca un producto en el inventario e imprime su nombre, precio y cantidad

  parametros:
  inventario

  retorna:
  nada
  """
  if len(inventario) == 0:
      print("No hay ningun producto todavia")
      return
  
  nombre = input("Ingresa el nombre del producto que vas a buscar: ")
  for producto in inventario:
      if producto["nombre"] != nombre: #Si el producto no es el que esta pidiendo el usuario continua al siguiente producto
          continue
      else:
          print("Producto encontrado")
          print(f"Nombre: {nombre} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
          return
  print("No se encontro el producto") 

def actualizar_producto(inventario):
    """
    Actualiza el precio y la cantidad de un producto ya registrado

    parametros:
    Inventario

    retorna:
    nada
    """
    if len(inventario) == 0:
        print("No hay ningun producto todavia")
        return
    nombre = input("Ingresa el nombre del producto que vas a actualizar: ")
    for producto in inventario:
      if producto["nombre"] != nombre: 
          continue
      else:
          precio = float(input("Ingresa el nuevo precio: "))
          cantidad = int(input("Ingresa la nueva cantidad: "))
          producto["precio"] = precio #Se le asigna el nuevo precio al producto
          producto["cantidad"] = cantidad #Se le asigna la nueva cantidad al producto
          print("Precio y cantidad actualizados")
          return
    print("Producto no encontrado")

def eliminar_producto(inventario):
    """
    Elimina un producto del inventario a partir del nombre

    parametros:
    Inventario

    retorna:
    nada
    """
    if len(inventario) == 0:
        print("No hay ningun producto todavia")
        return
    nombre = input("Ingresa el nombre del producto que vas a eliminar: ")
    for producto in inventario:
      if producto["nombre"] != nombre:
          continue
      else:
          inventario.remove(producto) #Si el nombre del producto en el bucle coincide con el nombre que ingreso el usuario se borra el producto
          print("Producto eliminado")
          return
    print("Producto no encontrado")