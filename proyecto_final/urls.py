from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('applications.jugador.urls')),

    path("", include('applications.categoria.urls')),
    path("", include('applications.busqueda.urls')),
  
    #para manejo de registro de usuarios
    #esta url esta en el codigo fuente de django automaticamente con muchas urls para manejo de usuarios
    path("accounts/",include('django.contrib.auth.urls')),

# concateno a este paquete de arrays otro para los multimedia
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#Que genere en base a este archivo media a esta configuración media URL que nos genere una web
# para la ruta de un documento que esté guardado en nuestro proyecto paralelo.