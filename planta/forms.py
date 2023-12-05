from django import forms

# la definicion de los tres formularios utilizando la clase forms 
# que recopila información sobre Alumnxs, Docentes y Salas.

class AlumnxFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    sala = forms.CharField()
    turno = forms.CharField()
    
class DocenteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    situacion_de_revista = forms.CharField()
    sala = forms.CharField()
    turno = forms.CharField()
    
class SalaFormulario(forms.Form):
    nombre = forms.CharField()
    cantidad_alumnxs = forms.IntegerField()
    turno = forms.CharField()
    docente = forms.CharField()
    