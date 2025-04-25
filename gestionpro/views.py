from django.shortcuts import render,redirect
from .models import Servicio
from .models import Mensaje

import base64

def index(request):
    return render(request, 'index.html')


def servicios(request):
    servicios = Servicio.objects.all()
    for s in servicios:
        s.imagen_base64 = base64.b64encode(s.imagen).decode('utf-8') if s.imagen else ""
    return render(request, 'servicios.html', {'servicios': servicios})

def mensajes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        Mensaje.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        return redirect('mensajes')  # Redirige a la misma página o a una de gracias

    return render(request, 'mensajes.html')