from funciones import *
carrito = []
respuesta = input("¿Desea agregar productos a su carrito: (no para salir)").lower()
while respuesta != 'no':
    nombre = input('Ingrese el nombre del producto:')
    precio = input('Ingrese el precio del producto:')
    cantidad = input('Ingrese las cantidades de su producto:')
    productos = agregar_producto(nombre,precio,cantidad)
    if isinstance(productos,dict):
        carrito.append(productos)
    else:
        print('Producto no agregado.')
    respuesta = input("¿Desea agregar productos a su carrito: (no para salir)").lower()

#mostrar_producto(carrito)
productos_unicos(carrito)
mostrar_resumen(carrito)
total = calcular_carrito(carrito)


descuento = aplicar_descuento(total)
total_iva = aplicar_IVA(total)
agregar_mensajes('hola','perrito','de','la','fama',sep = '-')
print(aplicar_descuento.__doc__)
