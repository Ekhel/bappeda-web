from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Dokumen


def beranda(request):
    context = {'title': 'Beranda | Bappeda Kab. Jayapura'}
    return render(request, 'home.html', context)


def produk(request):
    context = {
        'title': 'Produk',
        'produk': Dokumen.objects.all()
    }

    return render(request, 'produk.html', context)
