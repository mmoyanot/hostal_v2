from django import forms
from .models import habitacion

class habForm(forms.ModelForm):
    class Meta:
        model = habitacion
        fields = [
            'nroHabitacion',
	    'tipoHabitacion',
            'tipoCama',
            'accesorios',
            'precio',
            'estado_habitacion'       
        ]

class UpdateHabForm(forms.ModelForm):
    class Meta:
        model = habitacion
        fields = [
            'estado_habitacion'   
        ]
    