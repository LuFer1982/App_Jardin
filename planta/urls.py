from django.urls import path
from planta.views import crear_alumnx, crear_docente, crear_sala, busqueda_en_base

urlpatterns = [
    path('crear_alumnx/', crear_alumnx, name='crear_alumnx'),
    path('crear_docente/', crear_docente, name='crear_docente'),
    path('crear_sala/', crear_sala, name='crear_sala'),
    path('busqueda_en_base/', busqueda_en_base),
    ]