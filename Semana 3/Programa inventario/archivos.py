import os
def guardar_csv (inventario):
    if len(inventario) == 0:
       print("No hay nada para guardar")
       return
    if not os.path.isfile("Inventario.csv"):
        with open("Inventario.csv", "w") as archivo:
            archivo.write("Nombre,Precio,Cantidad")
    try:
        with open ("Inventario.csv","a") as archivo:
            for producto in inventario:
                archivo.writelines(["\n",producto["nombre"],",",str(producto["precio"]),",",str(producto["cantidad"])])
        print(f"Archivo guardado en la ruta: {os.path.abspath("Inventario.csv")}")
    except:
        print("Error,algo salio mal")

def cargar_csv (inventario):
    if not os.path.isfile("Inventario.csv"):
        print("No hay archivo para cargar")
        return
    else:
        inventario_temporal = []
        with open("Inventario.csv","r") as archivo:
            filas = archivo.read().splitlines()
            for fila in filas[1:]:
                producto_en_fila = fila.split(",")
                producto = {
                    "nombre":producto_en_fila[0],
                    "precio":float(producto_en_fila[1]),
                    "cantidad":int(producto_en_fila[2])
                }
                inventario_temporal.append(producto)
            print("Se cargo el inventario")
            intentos_cargar = 0
            while intentos_cargar != 3:
                que_hacer = input("Sobreescribir inventario actual? (S/N): ")
                if que_hacer == "S":
                    return inventario_temporal
                elif que_hacer == "N":
                    for producto_inventario_general in inventario:
                        for producto_inventario_temporal in inventario_temporal:
                            if producto_inventario_general["nombre"] == producto_inventario_temporal["nombre"]:
                                producto_inventario_general["precio"] = producto_inventario_temporal["precio"]
                                producto_inventario_general["cantidad"] += producto_inventario_temporal["cantidad"]
                                print("Se ejecuto")
                                break
                            else:
                                continue
                    print(f"Productos cargados: {len(inventario_temporal)}")
                    return inventario
                else:
                    print("Por favor escribe una opcion valida, S para si y N para no")
                    intentos_cargar += 1
