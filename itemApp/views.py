from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Reserva, Mesa
from .serializers import ReservaSerializer


def lista_reservas(request):
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    return render(
        request,
        'itemApp/lista_reservas.html',
        {'reservas': reservas}
    )


def crear_reserva_web(request):
    mesas = Mesa.objects.all()

    if request.method == 'POST':
        # Combinamos POST y FILES para que DRF procese todo correctamente
        data = request.POST.copy()
        serializer = ReservaSerializer(data=data)

        if serializer.is_valid():
            reserva = serializer.save()
            # Si subieron una imagen, la asignamos y guardamos directamente
            if 'imagen' in request.FILES:
                reserva.imagen = request.FILES['imagen']
                reserva.save()

            messages.success(request, "La reserva fue creada correctamente.")
            return redirect('lista_reservas')

        return render(
            request,
            'itemApp/crear_reserva.html',
            {
                'errores': serializer.errors,
                'mesas': mesas
            }
        )

    return render(
        request,
        'itemApp/crear_reserva.html',
        {'mesas': mesas}
    )


def editar_reserva_web(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    mesas = Mesa.objects.all()

    if request.method == 'POST':
        # Usamos partial=True para que no exija campos omitidos o la imagen
        serializer = ReservaSerializer(reserva, data=request.POST, partial=True)

        if serializer.is_valid():
            reserva_editada = serializer.save()

            # Solo actualizamos la imagen si la persona adjuntó un nuevo archivo
            if 'imagen' in request.FILES:
                reserva_editada.imagen = request.FILES['imagen']
                reserva_editada.save()

            messages.success(request, "La reserva fue modificada correctamente.")
            return redirect('lista_reservas')

        return render(
            request,
            'itemApp/editar_reserva.html',
            {
                'reserva': reserva,
                'mesas': mesas,
                'errores': serializer.errors
            }
        )

    return render(
        request,
        'itemApp/editar_reserva.html',
        {
            'reserva': reserva,
            'mesas': mesas
        }
    )


def eliminar_reserva_web(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        reserva.delete()
        messages.success(request, "La reserva fue eliminada correctamente.")
        return redirect('lista_reservas')

    return render(
        request,
        'itemApp/eliminar_reserva.html',
        {'reserva': reserva}
    )


@api_view(['GET'])
def api_lista_reservas(request):
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_crear_reserva(request):
    serializer = ReservaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'GET':
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReservaSerializer(reserva, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)