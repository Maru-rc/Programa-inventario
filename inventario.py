import Funciones #Aca importo las funciones del archivo Funciones.py
inventario = [] #Lista que guarda los diccionarios con el nombre precio y cantidad de producto
salir_bucle = 0 #Variable para salir del bucle While

#Este es el buclee While que ejecuta el codigo principal, osea el menu
while salir_bucle == 0:
    print("""
Hola, que quieres hacer?

1. Agregar Producto
2. Mostrar inventario
3. Calcular Estadisticas
4. Salir
          """)
    opcion = input("Escoge una opcion: ") #Variable que guarda la opcion que pone el usuario
     
    if opcion == "1":
        seguir_agregando = "si" #Variable para salir del bucle while de abajo
        while seguir_agregando != "no": #Bucle para agregar productos segun las veces que el usuario quiera
            Funciones.agregar_producto(inventario) #Aca se llama a la funcion que agrega los productos
            seguir_agregando = input("Quieres agregar otro producto? si/no: ") #si pone no se sale del bucle

    elif opcion == "2":
        print("\nInventario")
        Funciones.mostrar_inventario(inventario) #Aca se llama a la funcion que muestra el inventario

    elif opcion == "3":
        print("\nEstadisticas")
        Funciones.calcular_estadisticas(inventario) #Aca se llama a la funcion que calcula las estadisticas

    elif opcion == "4":
        print("Chao")
        salir_bucle = 1 #Aca se cambia el valor de la variable para salir del programa
    else:
        print("Ingresa una opcion valida") #Esto se ejecuta si ingresa algo diferente a las opciones dadas