from .cart import Cart

#Crearemos un procesador de contexto para que nuestro carrito pueda trabajar en todas las paginas
def cart(request):
    return {'cart': Cart(request)}