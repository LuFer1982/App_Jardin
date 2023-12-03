from django import forms

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
    