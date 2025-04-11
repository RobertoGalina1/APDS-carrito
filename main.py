from funciones import *
from estructura_avanzada import *
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
#productos_unicos(carrito)
#mostrar_resumen(carrito)
#total = calcular_carrito(carrito)


#descuento = aplicar_descuento(total)
#total_iva = aplicar_IVA(total)
#agregar_mensajes('hola','perrito','de','la','fama',sep = '-')
#print(aplicar_descuento.__doc__)

recorrer_lista(carrito)

productos = [
    {'nombre': 'carne', 'precio': 80, 'cantidad': 2},
    {'nombre': 'pollo', 'precio': 20, 'cantidad': 1},
    {'nombre': 'pescado', 'precio': 120, 'cantidad': 3},
    {'nombre': 'salmon', 'precio': 120, 'cantidad':1}
]   

print(filtrar_productos_caros(productos))
print(calcular_precios_con_descuentos(productos))