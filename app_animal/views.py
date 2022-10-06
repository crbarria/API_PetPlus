
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Animal

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class AnimalView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_animal=0):
        if (id_animal>0):
            animales=list(Animal.objects.filter(id_animal=id_animal).values())
            if len(animales) > 0:
                animal=animales[0]
                datos={'message':"Success",'animales':animal}
            else:
                datos={'message':"Animales no encontrados..."}
            return JsonResponse(datos)
        else:
            animales=list(Animal.objects.values())
            if len(animales)>0:
                datos={'message':"Success",'animales':animales}
            else:
                datos={'message':"Animales no encontrados..."}
            return JsonResponse(datos)
    
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Animal.objects.create(
            nombre=jd['nombre'],
            sexo=jd['sexo'],
            especie=jd['especie'],
            altura=jd['altura'],
            color=jd['color'],
            n_microchip=jd['n_microchip'],
            raza=jd['raza'],
            dueno_id_dueno_id=jd['dueno_id_dueno_id'],
            ficha_veterinaria_id_ficha_id=jd['ficha_veterinaria_id_ficha_id']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_animal):
        jd=json.loads(request.body)
        animales = list(Animal.objects.filter(id_animal=id_animal).values())
        if len(animales) > 0:
            animal=Animal.objects.get(id_animal=id_animal)
            animal.nombre=jd['nombre'],
            animal.sexo=jd['sexo'],
            animal.especie=jd['especie'],
            animal.altura=jd['altura'],
            animal.color=jd['color'],
            animal.n_microchip=jd['n_microchip'],
            animal.raza=jd['raza'],
            animal.dueno_id_dueno_id=jd['dueno_id_dueno_id'],
            animal.ficha_veterinaria_id_ficha_id=jd['ficha_veterinaria_id_ficha_id']
            animal.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"Animal not found"}
        return JsonResponse(datos)

    def delete(self,request, id_animal):
        animales = list(Animal.objects.filter(id_animal=id_animal).values())
        if len(animales) > 0:
            Animal.objects.filter(id_animal=id_animal).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Animal no encontrado"}
        return JsonResponse(datos)