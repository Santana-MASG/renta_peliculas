from .models import Pelicula
from django.forms import ModelForm

class Pelicula_Form(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'