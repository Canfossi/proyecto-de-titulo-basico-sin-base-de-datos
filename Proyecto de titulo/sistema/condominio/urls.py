from django.urls import path
from . import views


urlpatterns =[
    #esta parte nos permite acceder a la parte de creacion y muestreo de datos 
    path('',views.inicio,name='inicio'),
    path('usuario',views.usuario,name='usuario'),
    path('cliente',views.cliente,name='cliente'),
    path('cliente/crear',views.crear,name='crear'),
    path('cliente/editar',views.editar,name='editar'),
]