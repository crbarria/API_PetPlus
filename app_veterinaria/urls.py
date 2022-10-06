from django.urls import path
from .views import VeterinariaView

urlpatterns=[
    path('veterinaria/', VeterinariaView.as_view(), name='veterinarias'),
    path('veterinaria/<int:id_veterinarial>', VeterinariaView.as_view(), name='veterinaria by id')
]