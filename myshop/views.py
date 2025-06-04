from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Remera
from .forms import ContactoForm

def index(request):
    remeras = Remera.objects.all()
    ctx = {"remeras": remeras}
    return render(request, "myshop/index.html", ctx)

def contacto(request):
    return render(request, "myshop/contacto.html")

def detalle_remera(request, id):
    remera = get_object_or_404(Remera, id=id)
    ctx = {"remera": remera}
    return render(request, "myshop/detalle_remera.html", ctx)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Tu mensaje fue enviado con éxito. ¡Gracias por contactarnos!')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'myshop/contacto.html', {'form': form})