from django.contrib import admin
from django.urls import path
from prueba_pasada.views import simple, param, doble

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba1/', simple),
    path('parametro/<str:nombre>', param),
    path('info/<str:genero>/<int:edad>', doble)
]
