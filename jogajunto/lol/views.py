from django.shortcuts import render
import sqlite3

from django.views import generic
from .models import Fila

import sys
from subprocess import run, PIPE

class PlayerView(generic.ListView):
    template_name = 'lista-jogadores.html'
    model = Fila
    context_object_name = "jogadores"
    ordering = ['modal']


def home(request):

    return render(request, 'home.html')



def external(request):

    inp = request.POST.get('nome_invocador')
    inp2 = request.POST.get('fila')

    out = run([sys.executable, 'C:\\dev\\appRiot\\jogajunto\\lol\\scripts\\main.py', inp, inp2], shell=False, stdout=PIPE)
    # out2 = run([sys.executable, 'C:\\dev\\appRiot\\jogajunto\\lol\\test.py', inp2], shell=False, stdout=PIPE)
    # print(out)

    return render(request, 'home.html', {})
    # return render(request, 'home.html', {'data1': out, 'data2': out2})
    # return render(request, 'home.html', {})


def button(request):

    inp = request.POST.get('atualizar')

    out = run([sys.executable, 'C:\\dev\\appRiot\\jogajunto\\timer_del.py', inp], shell=False, stdout=PIPE)


    return render(request, 'home.html', {})


