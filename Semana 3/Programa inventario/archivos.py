import os
def guardar_csv (inventario):
    """
    Esto guarda el archivo csv, si no existe el archivo lo crea y le pone por defecto el header con Nombre,Precio,Cantidad,
    si el archivo existe agrega en el documento el nombre precio y cantidad de cada producto en el inventario

    Parametros:
    Inventario

    Retorna:
    Nada
    """
    if not os.path.isfile("Inventario.csv"): #Esto verifica si el archivo no existe
        with open("Inventario.csv", "w") as archivo:
            archivo.write("Nombre,Precio,Cantidad")#Si el archivo no existe lo crea y le pone el header
    try:
        if len(inventario) == 0:
            print("No hay nada para guardar")
            return
    except:
        print("No hay nada para guardar")
       
    try:
        with open ("Inventario.csv","a") as archivo:
            for producto in inventario:
                archivo.writelines(["\n",producto["nombre"],",",str(producto["precio"]),",",str(producto["cantidad"])]) #Aca se añade al archivo cada producto del inventario
        print(f"Archivo guardado en la ruta: {os.path.abspath("Inventario.csv")}")
    except:
        print("Error, solo se permite guardar texto")

def cargar_csv (inventario):
    """
    Esto carga el archivo csv y lo retorna al inventario

    Parametros:
    Inventario

    Retorna:
    Si el usuario presiona S retorna el inventario que esta en el archivo csv(inventario_temporal)
    Si el usuario presiona N retorna el inventario que esta en memoria(inventario) fusionado con el inventario que esta en el archivo csv(inventario_temporal)
    """
    if not os.path.isfile("Inventario.csv"): #Esto verifica si el archivo no existe
        print("No hay archivo para cargar")
        return 
    else:
        inventario_temporal = [] #esta lista va a tener los productos cargados desde el csv
        with open("Inventario.csv","r") as archivo:
            filas = archivo.readlines() #En esta varaible se guarda lo que hay en el archivo 
            contador_errores = 0
            for fila in filas[1:]: #Aca recorre cada fila del archivo, se empiza en 1 para volarse el header
                producto_en_fila = fila.split(",") #Aca se divide por comas
                if len(producto_en_fila) > 3 or len(producto_en_fila) < 3: #Esto es para que no haya filas invalidas
                    contador_errores += 1
                    continue
                if float(producto_en_fila[1]) < 0 or int(producto_en_fila[2]) < 0: #Para verificar que el precio y la cantidad no esten en negativo
                    contador_errores += 1
                    continue
                try:
                    producto = {
                        "nombre":producto_en_fila[0],
                        "precio":float(producto_en_fila[1]),
                        "cantidad":int(producto_en_fila[2])
                    } #Esto lo que hace es crear un diccionario del producto
                    inventario_temporal.append(producto)
                except ValueError: #Esto es por si se llega a cargar en el precio o la cantidad algo diferente a un numero
                    contador_errores += 1

            intentos_cargar = 0
            while intentos_cargar != 3:
                que_hacer = input("Sobreescribir inventario actual? (S/N): ").upper()
                if que_hacer == "S": #Si el usuario escribe S o s se carga el inventario que estaba en el csv y reemplaza el otro
                    print("Se remplazo el inventario")
                    print(f"Productos cargados: {len(inventario_temporal)}")
                    print(f"{contador_errores} filas invalidas omitidas")
                    return inventario_temporal 
                
                elif que_hacer == "N": #Si el usuario escribe N o n se fusiona el inventario del csv con el otro 
                    print("\nSi ya existe un producto se actualiza su precio por el cargado en el archivo,la cantidad se suma con la que ya habia")
                    if len(inventario) != 0: #Esto es para verificar que el inventario no este vacio
                        for producto_inventario_general in inventario: 
                            for producto_inventario_temporal in inventario_temporal:
                                if producto_inventario_general["nombre"] == producto_inventario_temporal["nombre"]: #Esto verifica si hay un producto con el mismo nombre en el inventario general y el inventario del csv
                                    producto_inventario_general["precio"] = producto_inventario_temporal["precio"] #Actualiza el precio del producto por el precio que tenia en el csv
                                    producto_inventario_general["cantidad"] += producto_inventario_temporal["cantidad"] #Suma la cantidad que habia en el inventario con la cantidad que habia en el csv
                                    break
                                else:
                                    continue
                    else: #Si el inventario llega a estar vacio se ejecuta esto
                        print("Se fusiono el inventario")
                        print(f"Productos cargados: {len(inventario_temporal)}")
                        print(f"{contador_errores} filas invalidas omitidas")
                        return inventario_temporal
                    
                    print("Se fusiono el inventario")
                    print(f"Productos cargados: {len(inventario_temporal)}")
                    print(f"{contador_errores} filas invalidas omitidas")
                    return inventario
                else:
                    print("Por favor escribe una opcion valida, S para si y N para no")
                    intentos_cargar += 1