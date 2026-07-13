from django.contrib import admin
from .models import Reserva, Mesa


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):

    list_display = (
        'numero',
        'capacidad'
    )

    search_fields = (
        'numero',
    )


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):

    list_display = (
        'nombre_persona',
        'telefono',
        'fecha_reserva',
        'hora_reserva',
        'estado',
        'mesa'
    )

    list_filter = (
        'estado',
        'fecha_reserva',
    )

    search_fields = (
        'nombre_persona',
        'telefono',
    )