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
    for elemento in lista:
        yield elemento 
    
