from django.contrib import admin

# Register your models here.

from planta.models import Docente, Alumnx, Sala

admin.site.register(Docente)
admin.site.register(Alumnx)
admin.site.register(Sala)