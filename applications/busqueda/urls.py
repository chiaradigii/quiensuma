from django.urls import path

app_name = "busqueda_app"
from . import views

urlpatterns = [
    path('lista-busquedas/',
    views.BusquedaListView.as_view(),
    name ='busquedas'
    ),
    path('nuevo-partido/',
    views.BusquedaCreateView.as_view(),
    name ='NuevoPartido'
    ),

]
