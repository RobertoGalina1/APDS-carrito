from decimal import Decimal

def agregar_producto(nombre,precio,cantidad):
    try:
        if not isinstance(nombre,str):
            raise TypeError("El nombre debe ser una string.")
        else:
            nombre = nombre.lower()
        
        precio = Decimal(precio)
        cantidad = int(cantidad)
        
        if precio < 0 or cantidad < 0:
            raise ValueError("Cantidades y precios deben ser mayores a 0.") 
            
    except Exception as e:
        return f'Se ha producido un error: {e}'
    
    else:
        diccionario = {'nombre':nombre,'precio':precio,'cantidad':cantidad, 'total':precio*cantidad}
        return diccionario

def mostrar_producto(lista):
    for elemento in lista:
        print(elemento)
        
def mostrar_resumen(lista):
    print("RESUMEN DE COMPRAS")
    print("-----------------------------------------------------------------------------")
    for numero,producto in enumerate(lista):
        print(f'{numero + 1} Producto {producto['nombre']} ||  {producto['cantidad']} x {producto['precio']} = {producto['cantidad'] * producto['precio']}')
        print("-----------------------------------------------------------------------------")
        
def calcular_carrito(lista):
    total = sum(map(lambda x:x['precio']*x['cantidad'],lista))
    print(f"El precio total de todo el carrito es: {total}$")
    return total