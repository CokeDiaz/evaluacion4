from rest_framework import serializers
from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = '__all__'


    def validate_cantidad_personas(self, value):

        if value < 1:
            raise serializers.ValidationError(
                "La cantidad de personas debe ser al menos 1."
            )

        if value > 15:
            raise serializers.ValidationError(
                "La cantidad máxima es 15 personas."
            )

        return value


    def validate_nombre_persona(self, value):

        if not value.strip():

            raise serializers.ValidationError(
                "Debe ingresar un nombre."
            )

        return value


    def validate_telefono(self, value):

        if not str(value).strip():

            raise serializers.ValidationError(
                "Debe ingresar un teléfono."
            )

        return value