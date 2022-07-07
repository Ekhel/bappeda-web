from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Dokumen, Kategori
from blogs.models import Article


def kategori(request):
    context = {
        'title': 'Kategori Dokumen',
        'kategori': Kategori.objects.all()
    }
    return render(request, 'kategori.html', context)


def produk(request, pk):
    kategori = Kategori.objects.get(id=pk)

    context = {
        'title': 'Produk',
        'kategori': kategori
    }

    return render(request, 'produk.html', context)
