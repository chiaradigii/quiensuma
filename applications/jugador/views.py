# Create your views here.
from django.views.generic import DetailView,CreateView,ListView,TemplateView
from .models import Jugador
from .forms import SingUpForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm



class SignUpView(CreateView):
     """Vista que usa el formulario de Django para 
         registrar un usuario"""
     model = Jugador
     template_name = "registration/signup.html"
     success_url= reverse_lazy('jugador_app:registroCorrecto')
     form_class= UserCreationForm
     
# class SignUpView(CreateView):
#      """Vista que usa el formulario de Django para 
#          registrar un jugeaodr/usuario"""
#      model = Jugador
#      template_name = "registration/signup.html"
#      success_url= reverse_lazy('jugador_app:registroCorrecto')
#      form_class= SingUpForm 

class JugadorCreateView(LoginRequiredMixin,CreateView):
    """Vista para registrar un jugeaodr"""
    """mixin para que solo me deje acceder si estoy authorizada"""
    model = Jugador
    template_name = "jugador/registrar_jugador.html"
    success_url= reverse_lazy('jugador_app:registroCorrecto')
    form_class= SingUpForm
    
class RegistroCorrecto(TemplateView):
    template_name = "jugador/registro_correcto.html"



class HomeView(TemplateView):
    """Vista que carga la pagina de inicio sin logueo"""
    template_name = "home.html"

class MainPageView(LoginRequiredMixin,TemplateView):
    """Vista que carga la pagina principal cuando alguien ya esta logueado"""
    template_name = "pagina_principal.html"



class JugadorListView(LoginRequiredMixin,ListView):
    # model = Jugador --> no hace falta porque sobre escribo uso query set
    template_name = "jugador/jugadores_disponibles.html"
    ordering = 'nombre'
    context_object_name = 'listaJugadores'
    paginate_by = 6


    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')

        filtrarTodo = Jugador.objects.filter(
            nombre__icontains= palabra_clave,
            #icontains busca palabra clave dentro de nombre 
            #si esta vacio no filtra
            #categoria__icontans = palabra_clave

        )
        return filtrarTodo

class JugadorDetailView(LoginRequiredMixin,DetailView):
    model = Jugador
    template_name = "jugador/detalle_jugador.html"
     
    def get_context_data(self, **kwargs):
        context = super(JugadorDetailView, self).get_context_data(**kwargs)
        return context
    






