from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.beranda, name="beranda"),
    path('', views.kategori, name="kategori"),
    path('dokumen/<str:pk>/', views.produk, name="produk"),
    path('aplikasi/', views.applikasi, name="aplikasi"),
]
