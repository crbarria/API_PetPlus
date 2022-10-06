
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import Veterinaria

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class VeterinariaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_veterinaria=0):
        if (id_veterinaria>0):
            veterinarias=list(Veterinaria.objects.filter(id_veterinaria=id_veterinaria).values())
            if len(veterinarias) > 0:
                veterinaria=veterinarias[0]
                datos={'message':"Success",'veterinarias':veterinaria}
            else:
                datos={'message':"veterinaria no encontrados..."}
            return JsonResponse(datos)
        else:
            veterinarias=list(Veterinaria.objects.values())
            if len(veterinarias)>0:
                datos={'message':"Success",'veterinarias':veterinarias}
            else:
                datos={'message':"veterinaria no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Veterinaria.objects.create(
            nombre_vet=jd['nombre_vet'],
            direccion=jd['direccion'],
            especialidad=jd['especialidad'],
            telefono=jd['telefono'],
            correo=jd['correo'],
            urgencia=jd['urgencia'],
            exoticos=jd['exoticos'],
            odontologia=jd['odontologia'],
            toma_muestras=jd['toma_muestras'],
            examenes=jd['examenes'],
            comuna_id_comuna=jd['comuna_id_comuna'],
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id_veterinaria):
        jd=json.loads(request.body)
        veterinarias = list(Veterinaria.objects.filter(id_veterinaria=id_veterinaria).values())
        if len(veterinarias) > 0:
            veterinaria=Veterinaria.objects.get(id_veterinaria=id_veterinaria)
            veterinaria.nombre_vet=jd['nombre_vet'],
            veterinaria.direccion=jd['direccion'],
            veterinaria.especialidad=jd['especialidad'],
            veterinaria.telefono=jd['telefono'],
            veterinaria.correo=jd['correo'],
            veterinaria.urgencia=jd['urgencia'],
            veterinaria.exoticos=jd['exoticos'],
            veterinaria.odontologia=jd['odontologia'],
            veterinaria.toma_muestras=jd['toma_muestras'],
            veterinaria.examenes=jd['examenes'],
            veterinaria.comuna_id_comuna=jd['comuna_id_comuna'],
            veterinaria.save()
            datos = {'mesage':"Success"}
        else:
            datos = {'message':"veterinaria not found"}
        return JsonResponse(datos)

    def delete(self,request, id_veterinaria):
        veterinarias = list(Veterinaria.objects.filter(id_veterinaria=id_veterinaria).values())
        if len(veterinarias) > 0:
            Veterinaria.objects.filter(id_veterinaria=id_veterinaria).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "veterinaria no encontrado"}
        return JsonResponse(datos)