from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home" ),
    path('addEmpresa/', views.addEmpresa, name="addEmpresa"),
    path('addComedor/', views.addComedor, name="addComedor"),
    path('cargarDatos/', views.cargarDatos, name="cargarDatos"),
    # path('listHab/', views.listaHab, name="listHab"),

]