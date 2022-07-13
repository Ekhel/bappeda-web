from django.shortcuts import render, redirect
from django.http import HttpResponse, response
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


def applikasi(request):
    context = {'title': 'Bappeda | Aplikasi'}

    return render(request, 'app.html', context)


# def struktur(request):
#     context = {'title': 'Bappeda | Struktur Organisasi'}

#     return render(request, 'nodedata.html', context)


def organisasi(request):
    context = {'title': 'Bappeda | Struktur Organisasi'}

    return render(request, 'struktur.html', context)
