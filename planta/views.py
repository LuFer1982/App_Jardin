from django.shortcuts import render
from planta.models import Docente, Alumnx, Sala
from planta.forms import AlumnxFormulario, DocenteFormulario, SalaFormulario



# Las vistas para crear docentes, alumnxs y salas.



def crear_docente(request):
                    
    if request.method == "POST":
        nuevo_formulario = DocenteFormulario(request.POST)   
                 
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_docente = Docente(
                    nombre=informacion["nombre"],
                    apellido=informacion["apellido"],
                    situacion_de_revista=informacion["situacion_de_revista"],
                    sala=informacion["sala"],
                    turno=informacion["turno"]
                    )
                
            nuevo_docente.save()
            return render(request, 'exito.html')
    else:
        nuevo_formulario = DocenteFormulario()
        return render(request, 'docente_formulario.html', {"formulario": nuevo_formulario})

def crear_alumnx(request):
    
    if request.method == "POST":
        nuevo_formulario = AlumnxFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_alumnx = Alumnx(
                    nombre=informacion["nombre"],
                    apellido=informacion["apellido"],
                    fecha_nacimiento =informacion["fecha_nacimiento"],
                    sala=informacion["sala"],
                    turno=informacion["turno"]
                    )
                
            nuevo_alumnx.save()
            return render(request, 'exito.html')
    else:
        nuevo_formulario = AlumnxFormulario()
        return render(request, 'alumnx_formulario.html', {"formulario": nuevo_formulario})
    
    
def crear_sala(request):
    
    if request.method == "POST":
        nuevo_formulario = SalaFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nueva_sala = Sala(
                    nombre=informacion["nombre"],
                    cantidad_alumnxs=informacion["cantidad_alumnxs"],
                    turno=informacion["turno"],
                    docente=informacion["docente"]
                    )
                
            nueva_sala.save()
            return render(request, 'exito.html')
    else:
        nuevo_formulario = SalaFormulario()
        return render(request, 'sala_formulario.html', {"formulario": nuevo_formulario})
    
#la vista para la busqueda de los alumnxs creados en la base

def busqueda_en_base (request):
    
    if request.method == "POST":
        busqueda = request.POST ['apellido']
        lista_alumnxs = Alumnx.objects.filter (apellido=busqueda)
    
        return render (request, 'lista_alumnxs.html', {'lista': lista_alumnxs})

    return render(request, "lista_alumnxs.html")