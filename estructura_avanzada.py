

def recorrer_lista(lista):
    """Version de mostrar producto usando un iter y next"""
    x = iter(lista)
    #VERSION 1
    while True:
        try:
            print(next(x))
        except StopIteration:
            print("Producto Desglozado finalizado")
            break
            
    #vERSION 2
    """
    i =0
    while i<len(lista):
        print(next(x))
        i += 1
    """    
       
def uno_por_uno(lista):
    """Se crea un generador capaz de no tener todo el archivo lista preparado solo cuando se llame se ejecuta"""
    for elemento in lista:
        yield elemento 
    
def combinar_productos(lista1,lista2,lista3):
    """Nos permite combinar productos [solo 3 listas]"""
    lista_tuplas = list(zip(lista1,lista2,lista3))
    print(lista_tuplas)
    #nombres,precios,cantidades = zip(*lista_tuplas)
    for elemento in lista_tuplas:
        nombre,precio,cantidad = elemento
        print(f'|| Producto {nombre} || Precio {precio:.3f} || Cantidad {cantidad}')
    
def combinar_productos2(*combinaciones):
    """Nos permite combinar productos [n listas]"""
    print(combinaciones)
    lista = list(zip(*combinaciones))
    for elemento in lista:
        nombre,precio,cantidad = elemento
        print(f'|| Producto {nombre} || Precio {precio:.3f} || Cantidad {cantidad}')

def filtrar_productos_caros(lista):
    productos_caros = [x for x in lista if x['precio']>50]
    return productos_caros

def calcular_precios_con_descuentos(lista,descuento=10):
    productos_descuento = [(x['precio']-x['precio']*descuento*0.01) if x['precio']>20 else x['precio'] for x in lista]
    for producto,precio in zip(lista,productos_descuento):
        producto['precio'] = precio
    return lista

def diccionario_descuento(*lista,descuento=10):   
    diccionario = {e[0]: (e[1]-e[1]*descuento*0.01) for e in lista if e[1]>30}
    return diccionario

def comparar_lista_productos(lista1,lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    union = set1.union(set2)
    inter = set1.intersection(set2)
    diff = set1.difference(set2)
    return union,inter,diff
#combinar_productos2(['carne','pollo','pescado'],[50.3,25.5,135.3],[2,1,5])

#combinar_productos3(['carne',50.3,2],['pollo',25.7,1],['pescado',121.5,5])


def gestionar_stock(stock,*varios):
    if input('Desea ingresar un producto en particular: ') == 'si':
        producto = input("Ingrese su producto: ")
        stock.add(producto)
    if input("Deseas agregar los productos guardados: ") == 'si':
        stock.update(varios)
    if input("Deseas eliminar un producto en particular: ") == 'si':
        try:
            eliminado = input('Ingrese el producto:')
            stock.discard(eliminado)
        except ValueError:
            print('Valor no encontrado en el stock')
    return stock
        
        

print(diccionario_descuento(['carne',50.3,2],['pollo',25.7,1],['pescado',121.5,5]))

cliente_a = ['carne', 'pollo', 'pescado', 'huevo', 'pan']
cliente_b = ['pollo', 'pescado', 'queso', 'leche', 'pan']
x,y,z = comparar_lista_productos(cliente_a,cliente_b)
print(x,y,z)
