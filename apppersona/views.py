from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, TarjetaJunaeb
from .forms import FormularioPersona

# Create your views here.
def lista_personas(request) : 
    # Queremos un contador de cuantas veces hemos visitado esta pagina.
    # No quiero usar las cookies directamente!!!
    # Voy a dejar que django maneje las cookies, y voy a usar una sesión de django.
    # recuperar el numero de visitas...
    # si el el valor no está almacenado previamente, se le da el valor del segundo param
    num_visitas = request.session.get('num_visitas', 0)
    num_visitas = num_visitas + 1
    # guardemos para la proxima vez.
    request.session['num_visitas'] = num_visitas

    # Queremos que nos muestre los datos de las personas....
    lista = Persona.objects.all() # todas las personas... 
    return render(request, 'apppersona/lista_personas.html'  , {'lista' : lista, 
        'num_visitas' : num_visitas})


def lista_tarjetas(request) :
    tarjetas = TarjetaJunaeb.objects.all() 
    return render(request, 'apppersona/lista_tarjetas.html',
        {'listaTarjetas' : tarjetas})

def tarjetas_con_plata(request) :
    tarjetas = TarjetaJunaeb.objects.filter(montoDisponible__gte=1) 
    # reutilizao el mismo template
    return render(request, 'apppersona/lista_tarjetas.html',
        {'listaTarjetas' : tarjetas})

def persona_nueva(request) :
    if request.method == 'POST' :
        formulario = FormularioPersona(request.POST) # formulario con los datos
        if formulario.is_valid() :
            persona = formulario.save(commit=False)
            persona.save() # guardamos la persona!
            return HttpResponse('Persona guardada')
    else :
        formulario = FormularioPersona()
    return render(request, 'apppersona/persona_nueva.html', {'form' : formulario})
