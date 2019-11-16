from django import forms
from .models import empresaDatos, comedorDatos, facturaDatos

class empresaForm(forms.ModelForm):

    class Meta:
        model = empresaDatos
        fields = [
            'rutEmpresa',
            'nombreEmpresa',
            'giroEmpresa',
            'dirEmpresa',
            'userEmpresa',
            'passEmpresa',
        ]

        labels = {
            'rutEmpresa' : 'Rut Empresa',
            'nombreEmpresa' : 'Nombre Empresa',
            'giroEmpresa' : 'Giro Empresa',
            'dirEmpresa' : "Dirección Empresa",
            'userEmpresa' : "Usuario",
            'passEmpresa': "Clave"
        }

        widgets = {
            'rutEmpresa' : forms.TextInput(attrs={'class':'form-control'}),
            'nombreEmpresa' : forms.TextInput(attrs={'class':'form-control'}),
            'giroEmpresa' : forms.TextInput(attrs={'class':'form-control'}),
            'dirEmpresa' : forms.TextInput(attrs={'class':'form-control'}),
            'userEmpresa' : forms.TextInput(attrs={'class':'form-control'}) ,
            'passEmpresa' : forms.PasswordInput(),
        }

class comedorForm(forms.ModelForm):
    class Meta:
        model = comedorDatos
        fields = [
            'tipoPlato',
            'entrada', 
            'platoFondo', 
            'postre', 
            'valorMenu', 
        ]

        labels = {
            'tipoPlato' : 'Tipo de plato',
            'entrada' : 'Entrada', 
            'platoFondo' : 'Plato de fondo', 
            'postre' : 'Postre', 
            'valorMenu' : 'Valor Menu', 
        }

        widgets = {
            'tipoPlato': forms.TextInput(attrs={'class':'form-control'}),
            'entrada': forms.TextInput(attrs={'class':'form-control'}), 
            'platoFondo': forms.TextInput(attrs={'class':'form-control'}), 
            'postre': forms.TextInput(attrs={'class':'form-control'}), 
            'valorMenu': forms.TextInput(attrs={'class':'form-control'}),             
        }

class facturaForm(forms.ModelForm):
    class Meta:
        model = facturaDatos
        fields = [
            'tipo_Serv_Fac', 
            'tipo_Hab_Fac', 
        ]

        labels = {
            'tipo_Serv_Fac' : 'Tipo de servicio', 
            'tipo_Hab_Fac' : 'Tipo de Habitación', 
        }

    


