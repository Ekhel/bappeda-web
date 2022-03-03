from multiprocessing import context
from django.shortcuts import render, redirect


def beranda(request):
    context = {'title': 'Beranda | Bappeda Kab. Jayapura'}
    return render(request, 'home.html', context)
