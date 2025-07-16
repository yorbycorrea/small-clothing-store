from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #obtener la clave de sesión actual si existe
        cart = self.session.get('session_key')
        
        #Si el usuario es nuevo, ¡sin clave de sesión! crea ahora
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
            
        #Nos aseguramos que el carrito este disponible en todas las paginas
        self.cart = cart    
        
    def add(self, product):
        product_id = str(product.id)
        
        #Logica
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}    
            
        self.session.modified = True 
    
    def __len__(self):
        return len(self.cart) 
    
    def get_prods(self):
        #Obtener el id del carrito
        product_ids = self.cart.keys()
        #Usa el ID para buscar producto en la base de datos
        products = Product.objects.filter(id__in=product_ids)
        #Retorna los productos buscados
        return products
        
              