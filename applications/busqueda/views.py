from django.shortcuts import render
from django.urls import reverse_lazy

from applications.jugador.models import Jugador
from .models import Busqueda
from django.views.generic import ListView,TemplateView,CreateView

class BusquedaListView(ListView):

    template_name = "busquedas/lista_busquedasV2.html"
    ordering = 'fecha'
    context_object_name = 'listaBusquedas'
    paginate_by = 6
    model = Busqueda #si tengo el query set no hace falta
    # def get_queryset(self):
    #     palabra_clave = self.request.GET.get("keyword",'')
        
    #     filtrarTodo = Jugador.objects.filter(
    #         localidad = palabra_clave      
    #     )
    #     return filtrarTodo


class BusquedaCreateView(CreateView):
    model = Busqueda
    template_name = "busquedas/nuevo_partido.html"
    fields = '__all__'
    success_url= reverse_lazy('jugador_app:registroCorrecto')

class RegistroCorrecto(TemplateView):
    template_name = "jugador/registro_correcto.html"