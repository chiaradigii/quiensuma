from django.urls import path


from . import views

app_name = "jugador_app"

urlpatterns = [
    
    #pagina de inicio
    path("",
     views.HomeView.as_view(),
     name='home',
     ),
     path("pagina-principal/",
     views.MainPageView.as_view(),
     name='pagina_principal',
     ),
     path("Felicidades/",
     views.RegistroCorrecto.as_view(),
     name='registroCorrecto',
     ),

     path('registrar-jugador/',
     views.JugadorCreateView.as_view(),
     name='registrar_jugador',
    ),
    path('jugadores-disponibles/',
    views.JugadorListView.as_view(),
    name='jugadores_disponibles',
    ),
    path('detalle-jugador/<pk>/',
    views.JugadorDetailView.as_view(),
    name='jugador_detalle',
    ),
  path('signup/',
     views.SignUpView.as_view(),
     name='signup',
    ),
    

]