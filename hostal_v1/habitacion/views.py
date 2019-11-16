from django.shortcuts import render, redirect
from django.contrib import messages

from .models import tipoCama, habitacion
from .forms import habForm, UpdateHabForm
# Create your views here.

def listaHab(request):
    queryset = habitacion.objects.all()
    context = {
        'listHab' : queryset
    }
    return render(request,"listaHabitaciones.html", context)

def addHab(request):
    queryset = habitacion.objects.all()

    form = habForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = habForm()
        messages.success(request, "Información guardada exitosamente")
        return redirect("addHab")

    context = {
        'listHab' : queryset,
        'form' : form

    }
    return render(request,"addHab.html", context)

def borrar(request,id_habitacion):
    item = habitacion.objects.get(id=id_habitacion)
    item.delete()
    #no envia el mensajito :c
    messages.success(request, ('El producto ha sido eliminado'))
    return redirect("listHab")

def editHab(request,id_habitacion):
   # llamando datos de habitacion seleccionada
    hab = habitacion.objects.get(id=id_habitacion)
    queryset = habitacion.objects.all()
    if request.method == 'GET':
        form = UpdateHabForm(instance=hab) 
    else:
        form = UpdateHabForm(request.POST, instance=hab)
        if form.is_valid():
            form.save()
            messages.success(request, "Estado de habitación actualizado")
        return redirect("listHab")
    context = {
        'form' : form,
        'hab' : hab,
        'listHab' : queryset
    }
    return render(request,"editEstHab.html",context)

