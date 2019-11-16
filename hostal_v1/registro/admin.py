from django.contrib import admin
from .models import empresaDatos, comedorDatos, facturaDatos

# Register your models here.
admin.site.register(empresaDatos)
admin.site.register(comedorDatos)
admin.site.register(facturaDatos)

