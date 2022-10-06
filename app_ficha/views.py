import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import FichaVeterinaria
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class FichaVeterinariaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def get(self,request,id_ficha=0):
        if (id_ficha>0):
            fichas=list(FichaVeterinaria.objects.filter(id_ficha=id_ficha).values())
            if len(fichas) > 0:
                ficha=fichas[0]
                datos={'message':"Success",'id_ficha':ficha}
            else:
                datos={'message':"fichas no encontrados..."}
            return JsonResponse(datos)
        else:
            fichas=list(FichaVeterinaria.objects.values())
            if len(fichas)>0:
                datos={'message':"Success",'fichas':fichas}
            else:
                datos={'message':"Comuunas no encontrados..."}
            return JsonResponse(datos)
        
def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        FichaVeterinaria.objects.create(
            id_ficha=jd['id_ficha'],
            ficha=jd['ficha']        
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

def put(self,request,id_ficha):
        jd=json.loads(request.body)
        fichas = list(FichaVeterinaria.objects.filter(id_ficha=id_ficha).values())
        if len(fichas) > 0:
            ficha=FichaVeterinaria.objects.get(id_ficha=id_ficha)
            ficha.estado=jd['ficha'],
            ficha.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"ficha not found"}
        return JsonResponse(datos)


def delete(self,request, id_ficha):
        fichas = list(FichaVeterinaria.objects.filter(id_ficha=id_ficha).values())
        if len(fichas) > 0:
            FichaVeterinaria.objects.filter(id_ficha=id_ficha).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Ficha no encontrado"}
        return JsonResponse(datos)
