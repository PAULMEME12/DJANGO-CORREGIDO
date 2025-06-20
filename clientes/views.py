from django.shortcuts import render, redirect
from .models import Cliente

def landing(request):
    return render(request, 'clientes/landing.html')

def formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        Cliente.objects.create(nombre=nombre, email=email)
        return redirect('landing')
    return render(request, 'clientes/formulario.html')

def listado(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado.html', {'clientes': clientes})