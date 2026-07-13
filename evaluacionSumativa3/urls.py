"""
URL configuration for evaluacionSumativa3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from itemApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.lista_reservas, name='lista_reservas'),
    path('crear/', views.crear_reserva_web, name='crear_reserva'),
    path('editar/<int:reserva_id>/', views.editar_reserva_web, name='editar_reserva'),
    path('eliminar/<int:reserva_id>/', views.eliminar_reserva_web, name='eliminar_reserva'),

    path('api/reservas/', views.api_lista_reservas, name='api_reservas'),
    path('api/reservas/<int:pk>/', views.detalle_reserva, name='api_reserva_detalle'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtener'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]