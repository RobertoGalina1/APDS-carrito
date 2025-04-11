from decimal import Decimal

def agregar_producto(nombre,precio,cantidad):
    """Funcion que me permite crear un diccionario al cual le pasaremos el nombre, precio y cantidad
        Devolveremos un dict con 4 keys
    """
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

def mostrar_resumen(lista):
    """Muestra un resumen con un formato más profesional y agradable a la vista"""
    print("RESUMEN DE COMPRAS")
    print("-----------------------------------------------------------------------------")
    for numero,producto in enumerate(lista,start=1):
        print(f"{numero} Producto {producto['nombre']} ||  {producto['cantidad']} x {producto['precio']} = {producto['cantidad'] * producto['precio']}")
        print("-----------------------------------------------------------------------------")
        #Cambie las comillas, agregar al tercer commit ese cambio
        
        
def calcular_total_carrito(lista):
    """Calcula el total de todo lo que llevamos en nuestro carrito"""
    total = sum(map(lambda x:x['precio']*x['cantidad'],lista))
    print(f"El precio total de todo el carrito es: {total}$")
    return total

def aplicar_descuento(total,descuento=10):
    """Aplicamos un descuento a nuestro total por defecto es de 10 por ciento"""
    lambda_fun = lambda x,y: x - x*y*Decimal(0.01)
    desc = lambda_fun(total,descuento)
    #print(f'Precio total sin descuento: {total}$')
    print(f'Precio total con descuento del {descuento}%: {round(desc,2)}$')
    return desc

def aplicar_IVA(total):
    """Aplicamos el impuesto al valor adquirido (IVA) a nuestro total"""
    iva = Decimal(0.16)
    lambda_fun = lambda x,y: x + x*y
    total_iva = lambda_fun(total,iva)
    #print(f'Precio total sin descuento: {total}$')
    print(f'Precio total con IVA incluido ({round(iva*100)})%: {round(total_iva,2)}$')
    return total_iva

def productos_unicos(lista):
    """Devuelve la cantidad de producto unicos y cuales son """
    unicos = set(map(lambda x: x["nombre"],lista))
    print(f'Tienes un total de {len(unicos)} productos distintos: {unicos}')
    
def agregar_mensajes(*mensajes,**caracteristicas):
    """Imprime un mensaje formado por args y caracteristicas con args"""
    palabra = " ".join(mensajes)
    for k,v in caracteristicas.items():    
        if k.lower() == 'mayus':
            if v == True:
                palabra = palabra.upper()
        elif k.lower() =='sep':
            palabra = v.join(palabra.split())
    print(palabra)

"""
def mostrar_producto(lista):
Muestra los elementos como diccionario - formato básico
    for elemento in lista:
        print(elemento) 
        
"""  
    
#agregar_mensajes('guan','paco','pedro','adios',mayus = True,sep = "-")
