#Se declaran las variables
precio_producto = 0
cantidad_producto = 0
 
#Variable que pide el nombre del producto
nombre_producto = input("Ingresa el nombre del producto: ")
 
#Esto es para que en dado caso coloque algo diferente a un numero no se reviente el programa y le mande un mensaje de error
try:
    precio_producto = float(input("Ingresa el precio del producto: ")) #Variable que pide el precio del producto
except ValueError:
    print("Por favor ingresa un valor valido")
    precio_producto = float(input("Ingresa el precio del producto: "))
 
#Hace lo mismo que la de arriba
try:
    cantidad_producto = int(input("Ingresa la cantidad que vas a llevar: ")) #Varaible que pide la cantidad de producto
except ValueError:
    print("Por favor ingresa una cantidad valida")
    cantidad_producto = int(input("Ingresa la cantidad que vas a llevar: "))
 
#Variable que calcula el costo total multiplicando la cantidad por el precio
costo_total = cantidad_producto * precio_producto 
 
#Aca se imprime todo, nombre del producto, el precio la cantidad y el costo total
print(f"\nProducto: {nombre_producto} | Precio: ${precio_producto} | cantidad: {cantidad_producto} | Total: ${costo_total}") 
 
 
 
#Este es un programa que permite registrar productos, calcula el costo total en base al precio y a la cantidad de producto que ingrese el usuario