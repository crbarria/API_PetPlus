from django.urls import path
from .views import FichaVeterinariaView


urlpatterns=[
    path('ficha_veterinaria/', FichaVeterinariaView.as_view(), name='ficha_veterinaria'),
    path('ficha_veterinaria/<int:id_ficha>', FichaVeterinariaView.as_view(), name='ficha_veterinaria by id')
]