from django.contrib import admin
from .models import Persona, TarjetaJunaeb

# Registramos el modelo de Persona para que django lo use.
admin.site.register(Persona)
admin.site.register(TarjetaJunaeb)