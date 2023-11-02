class carrito:

    def __init__(self,request):
        self.request=request  #almacenar la peticion en la variable request
        self.session=request.session #almacenar la sesion de usuario 
        carrito=self.session.get("carrito")#si esta iniciada la sesion aparece el carrito
        if not carrito: #Si no hay carrito es un diccionario que esta vacio
            carrito=self.session["carrito"]={}

        self.carrito=carrito #el carrito es igual al carrito que ya tenias si fuiste de la plataforma

    #agregar productos
    def agregar(self,producto):
        if(str(producto.id)not in self.carrito.keys()): #si el id del producto no esta en la claves del carrito lo agregas
            self.carrito[producto.id]={          #
                "producto_id":producto.id,     # 
                "nombre":producto.title,      #  Agregar un producto al carrito
                "precio":str(producto.price), #
                "cantidad":1,                  #
                "imagen":producto.image.url   #
            }
        else: #en caso de que el id si este en el carrito entonces:
            for key, value in self.carrito.items():
                if key==str(producto.id):                       # camprueba si la clave corresponde con 
                    value["cantidad"]=value["cantidad"]+1       # algo que ya esta en el carrito para esa 
                    value["precio"]=float(value["precio"])+producto.price
                    break                                       # clave la cantidad se incrementara                                                        
        #funcion para actualizar la sesion cada vez que se haga alguna operacion en el carrito
        self.guardar_carro()
    def guardar_carro(self):
        self.session["carrito"]=self.carrito #el carrito tiene que ser igual a al carrito de la sesion que se este manejando en ese momento
        self.session.modified=True

    #eliminar productos
    def eliminar(self,producto):
        producto.id=str(producto.id) #el id del producto tiene que ser igual al id pasado a stream
        if producto.id in self.carrito: #si ese producto esta en el carrito:
            del self.carrito[producto.id] #lo quitas 
            #despues de que el producto es eliminado se tiene que volver a guardar el carrito
            self.guardar_carro()

    #restar unidades de un producto
    def restar_producto(self, producto):
        for key, value in self.carrito.items():                    # camprueba si la clave corresponde con 
                if key==str(producto.id):                       # algo que ya esta en el carrito para esa 
                    value["cantidad"]=value["cantidad"]-1       # clave la cantidad se reduce y si la 
                    value["precio"]=float(value["precio"])-producto.price
                    if value["cantidad"]<1:                     # cantidad de pruductos es menor a 1 
                        self.eliminar(producto)                 # entonces se eliminara ese producto
                    break                                       
        self.guardar_carro()
    
    #vaciar carrito
    def limpiar_carro(self):
        carrito=self.session["carrito"]={}
        self.session.modified=True



