from multiprocessing import context
from django.shortcuts import render, redirect


def beranda(request):
    context = {'title': 'Badan Perencanaan Pembangunan Daerah'}
    return render(request, 'home.html', context)
