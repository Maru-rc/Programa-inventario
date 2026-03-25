import servicios 
import archivos
inventario = [] #Este es el inventario donde se van a guardar todos los productos, los productos se guardan como diccionarios
salir_bucle = 0 

while salir_bucle == 0:
    print("""
Hola, que quieres hacer?

1. Agregar Producto
2. Mostrar inventario
3. Calcular Estadisticas
4. Buscar producto
5. Actualizar producto
6. Eliminar producto
7. Guardar CSV
8. Cargar CSV
9. Salir
          """)
    opcion = input("Escoge una opcion: ") 
     
    if opcion == "1":
        seguir_agregando = "si" 
        while seguir_agregando != "no": 
            servicios.agregar_producto(inventario) 
            seguir_agregando = input("Quieres agregar otro producto? si/no: ").lower()

    elif opcion == "2":
        print("\nInventario")
        servicios.mostrar_inventario(inventario) 

    elif opcion == "3":
        print("\nEstadisticas")
        servicios.calcular_estadisticas(inventario) 

    elif opcion == "4":
        servicios.buscar_producto(inventario)
    
    elif opcion == "5":
        servicios.actualizar_producto(inventario)
    
    elif opcion == "6":
        servicios.eliminar_producto(inventario)
    
    elif opcion == "7":
        archivos.guardar_csv(inventario)
    
    elif opcion == "8":
        inventario = archivos.cargar_csv(inventario)

    elif opcion == "9":
        print("Chao")
        salir_bucle = 1
    else:
        print("Ingresa una opcion valida")