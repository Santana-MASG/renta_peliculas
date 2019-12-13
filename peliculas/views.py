from django.shortcuts import redirect, render
from peliculas.models import Pelicula, Renta, Detalle_Renta
from django.contrib.auth.decorators import login_required
from .forms import Pelicula_Form
import datetime
# Create your views here.

@login_required
def peliculas(request):
    if request.method == 'POST':
        form = Pelicula_Form(request.POST)
        for campo in form.data:
            if not campo.isnumeric():
                continue
            pelicula = Pelicula.objects.get(id=int(campo))
            renta = Renta.objects.create(usuario=request.user, fecha=datetime.datetime.today())
            Detalle_Renta.objects.create(renta=renta, pelicula=pelicula)
            pelicula.stock -= 1
            pelicula.save()
        return redirect('peliculas')
    else:
        form = Pelicula_Form()
    peliculas = Pelicula.objects.all()
    return render(request, 'renta_peliculas.html',{'peliculas': peliculas})
