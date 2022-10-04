from django.urls import path
from .views import AnimalView

urlpatterns=[
    path('animal/', AnimalView.as_view(), name='animal_lista'),
    path('animal/<int:id_animal>', AnimalView.as_view(), name='animal_process')

]