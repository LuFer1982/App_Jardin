from django.contrib import admin

# el registro de los 3 modelos que tengo

from planta.models import Docente, Alumnx, Sala

admin.site.register(Docente)
admin.site.register(Alumnx)
admin.site.register(Sala)