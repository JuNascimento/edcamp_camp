from django.shortcuts import render
from django.utils import timezone
from .models import Campeonato
from django.shortcuts import render, get_object_or_404

# Create your views here.

def lista_campeonatos(request):
	campeonato_list = Campeonato.objects.order_by('campeonato_id')
	return render(request,'campeonatos/lista_campeonatos.html', {'campeonato_list': campeonato_list})
	# return render(request,'campeonatos/lista_campeonatos.html', {})

def campeonato_detalhe(request, pk):
    campeonato = get_object_or_404(Campeonato, pk=pk)
    return render(request, 'campeonatos/campeonato_detalhe.html', {'campeonato': campeonato})