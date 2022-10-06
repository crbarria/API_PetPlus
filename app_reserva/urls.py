from django.urls import path
from .views import ReservaHorasView

urlpatterns=[
    path('reserva/', ReservaHorasView.as_view(), name='reserva'),
    path('reserva/<int:id_reserva_horas>', ReservaHorasView.as_view(), name='reserva by id')
]