from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


ESTADOS_RESERVA = [
    ('COMPLETADA', 'Completada'),
    ('ANULADA', 'Anulada'),
    ('NO_ASISTEN', 'No asisten'),
]


class Mesa(models.Model):

    numero = models.PositiveIntegerField(
        unique=True
    )

    capacidad = models.PositiveIntegerField()

    def __str__(self):

        return f"Mesa {self.numero}"


class Reserva(models.Model):

    nombre_persona = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=20
    )

    fecha_reserva = models.DateField()

    hora_reserva = models.TimeField()

    cantidad_personas = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15)
        ]
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_RESERVA
    )

    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.CASCADE
    )

    observacion = models.TextField(
        blank=True
    )

    def __str__(self):

        return (
            f"{self.nombre_persona} - "
            f"{self.fecha_reserva}"
        )