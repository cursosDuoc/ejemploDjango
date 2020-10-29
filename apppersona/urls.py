from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('persona/nueva', views.persona_nueva, name='persona_nueva'),
    path('tarjetas', views.lista_tarjetas, name='lista_tarjetas'),
    path('tarjetas_con_plata', views.tarjetas_con_plata, name='tarjetas_con_plata'),
]