from carrito.carrito import carrito

def importe_total_carro(request): #request es un parametro que permite el acceso a toda la información que pasa desde el navegador del cliente al servidor.
    total=0
    carro=carrito(request)
    if request.user.is_authenticated:  #si el usuario esta autenticado entonces:
        for key, value in carro.carrito.items():
       #para cada elemnto del carro 
            total=total+float(value["precio"])  #incrementara el total
    else:
        total="Debes hacer login"
    return {"importe_total_carro":total}
