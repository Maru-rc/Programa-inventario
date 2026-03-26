import os
def guardar_csv(inventario):
    """
    Esto guarda el archivo csv, si no existe el archivo lo crea y le pone por defecto el header con Nombre,Precio,Cantidad,
    si el archivo existe agrega en el documento el nombre precio y cantidad de cada producto en el inventario

    Parametros:
    Inventario

    Retorna:
    Nada
    """
    opcion = input("¿Quieres usar el nombre de archivo por defecto 'Inventario.csv'? (si/no): ").lower()
    escogio_bien = False
    intentos_bucle = 0
    while escogio_bien == False:
        if intentos_bucle == 3:
            print("Error, numero maximo de intentos alcanzado")
            return
        if opcion == "si":
            nombre_archivo = "Inventario.csv"
        elif opcion == "no":
            nombre_archivo = input("Ingresa el nombre del archivo: ")
            nombre_archivo_partido = nombre_archivo.split(".")
            if nombre_archivo.count(".") < 1: #Si no puso ningun punto, osea que no definio el tipo de archivo, se define como csv
                nombre_archivo += ".csv"
                break
            if nombre_archivo_partido[-1] != "csv": #Si llega a intentar guardar el archivo como algo diefernte a un csv, por ejemplo un json, se cambia y se define como csv
                nombre_archivo_partido[-1] = "csv"
                nombre_archivo = ".".join(nombre_archivo_partido)
        else:
            print("Por favor escoge si o no")
            intentos_bucle += 1

    if not os.path.isfile(nombre_archivo): 
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Nombre,Precio,Cantidad")
    try:
        if len(inventario) == 0:
            print("No hay nada para guardar")
            return
    except:
        print("No hay nada para guardar")
       
    try:
        with open(nombre_archivo, "a") as archivo:
            for producto in inventario:
                archivo.writelines(["\n", producto["nombre"], ",", str(producto["precio"]), ",", str(producto["cantidad"])]) #Aca se añade al archivo cada producto del inventario
        print(f"Archivo guardado en la ruta: {os.path.abspath(nombre_archivo)}")
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
    nombre_archivo = input("Ingresa el nombre del archivo a cargar: ")
    nombre_archivo_partido = nombre_archivo.split(".")
    if nombre_archivo_partido[-1] != "csv": #Verifica si el archivo no es csv
        print("Solo se pueden cargar archivos csv")
        return
    if not os.path.isfile(nombre_archivo): #Esto verifica si el archivo no existe
        print("El archivo no existe")
        return 
    else:
        inventario_temporal = [] #esta lista va a tener los productos cargados desde el csv
        with open(nombre_archivo,"r") as archivo:
            filas = archivo.readlines() #En esta varaible se guarda lo que hay en el archivo 
            if filas[0] != "nombre,precio,cantidad": #Esto es para verificar que el header sea valido, si no lo es no se guarda nada y vuelve al menu
                print("No se pudo cargar el archivo porque tiene encabezado invalido")
                return
            contador_errores = 0
            for fila in filas[1:]: #Aca recorre cada fila del archivo, se empiza en 1 para volarse el header
                producto_en_fila = fila.split(",") #Aca se divide por comas
                if len(producto_en_fila) > 3 or len(producto_en_fila) < 3: #Esto es para que no haya filas invalidas
                    contador_errores += 1
                    continue
                try:
                    if float(producto_en_fila[1]) < 0 or int(producto_en_fila[2]) < 0: #Para verificar que el precio y la cantidad no esten en negativo
                        contador_errores += 1
                        continue
                except ValueError:
                    contador_errores +=1
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