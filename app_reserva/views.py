import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from .models import ReservaHoras

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class ReservaHorasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id_reserva_horas=0):
        if (id_reserva_horas>0):
            reservas=list(ReservaHoras.objects.filter(id_reserva_horas=id_reserva_horas).values())
            if len(reservas) > 0:
                reserva=reservas[0]
                datos={'message':"Success",'reservas':reserva}
            else:
                datos={'message':"reservas no encontrados..."}
            return JsonResponse(datos)
        else:
            reservas=list(ReservaHoras.objects.values())
            if len(reservas)>0:
                datos={'message':"Success",'reservas':reservas}
            else:
                datos={'message':"reservas no encontrados..."}
            return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        ReservaHoras.objects.create(
            horas=jd['horas'],
            veterinaria_id_veterinaria=jd['veterinaria_id_veterinaria'],
            estado_hora_id_estado_hora=jd['estado_hora_id_estado_hora']    
            )
        datos={'message':"Success"}
        return JsonResponse(datos)



    def put(self,request,id_reserva_horas):
        jd=json.loads(request.body)
        reservas = list(ReservaHoras.objects.filter(id_reserva_horas=id_reserva_horas).values())
        if len(reservas) > 0:
            reserva=ReservaHoras.objects.get(id_reserva_horas=id_reserva_horas)
            reserva.horas=jd['horas'],
            reserva.veterinaria_id_veterinaria=jd['veterinaria_id_veterinaria'],
            reserva.estado_hora_id_estado_hora=jd['estado_hora_id_estado_hora']
            reserva.save()
            datos = {'mesage':"Succes"}
        else:
            datos = {'message':"reserva not found"}
        return JsonResponse(datos)



    def delete(self,request, id_reserva_horas):
        reservas = list(ReservaHoras.objects.filter(id_reserva_horas=id_reserva_horas).values())
        if len(reservas) > 0:
            ReservaHoras.objects.filter(id_reserva_horas=id_reserva_horas).delete()
            datos = {'message' : "succes"}
        else:
            datos = {'message' : "Reserva no encontrado"}
        return JsonResponse(datos)