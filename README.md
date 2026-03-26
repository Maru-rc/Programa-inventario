# Programa inventario python

## Descripción
Este programa en Python permite gestionar un inventario de productos desde la consola. El usuario puede agregar productos con su nombre, precio y cantidad, y el programa se encarga de mantener todo organizado en memoria. También permite exportar e importar el inventario usando archivos CSV para no perder los datos entre sesiones.


## Funcionalidades
- **Agregar productos:** Agrega un producto con su nombre, precio y stock.
- **Mostrar inventario:** Muestra todos los productos registrados con su nombre precio y stock.
- **Estadísticas:** Calcula el valor total del inventario, cuántos productos hay registrados, el producto más caro y el que tiene mayor stock.
- **Buscar producto:** Encuentra un producto por su nombre y muestra su precio y stock.
- **Actualizar producto:** Permite cambiar el precio y la cantidad de un producto ya registrado.
- **Eliminar producto:** Borra un producto del inventario por nombre.
- **Guardar CSV:** Exporta el inventario a un archivo `.csv`.
- **Cargar CSV:** Carga un archivo `.csv` y permite fusionarlo con el inventario actual o reemplazarlo.

## Ejemplo
```
Ingresa el nombre del producto: Manzana
Ingresa el precio del producto: 1500
Ingresa la cantidad que vas a llevar: 10

Producto: Manzana | Precio: $1500.0 | Cantidad: 10
```

## Formato del CSV
El archivo debe tener el siguiente encabezado para poder ser cargado correctamente:
```
Nombre,Precio,Cantidad

```

## Estructura del proyecto
```
├── app.py          # Menú principal, donde se ejecuta el programa
├── servicios.py    # Archivo donde estan las funciones (agregar, buscar, actualizar, eliminar)
└── archivos.py     # Archivo con funciones para guardar y cargar archivos csv
```

## Tecnologías usadas
- Python
