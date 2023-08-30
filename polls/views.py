from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import Mypro


# Create your views here.


def index(request):
    model = Mypro.objects.all()
    result0 = []
    for i in model:
        result0.append({
            'f_name': i.f_name,
            'l_name': i.l_name
        })
        return JsonResponse(result0, safe=False)

    def detail(request, my_id):
        data = get_list_or_404(Mypro, pk=my_id)
        result = {
            'f.name': data.f_name,
            'l.name': data.l_name
        }
        return JsonResponse(result, safe=False)
