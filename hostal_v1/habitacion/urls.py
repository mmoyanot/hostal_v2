from django.urls import path
from . import views

urlpatterns = [
    path('listHab/', views.listaHab, name="listHab"),
    path('addHab/', views.addHab, name="addHab"),
    path('editEstHab/<id_habitacion>', views.editHab, name="editEstHab"),
    path('delete/<id_local>/<list_id>', views.borrar, name="borrar"),
]