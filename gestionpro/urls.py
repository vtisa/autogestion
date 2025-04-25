from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('mensajes/', views.mensajes, name='mensajes'),
]
