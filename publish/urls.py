from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.beranda, name="beranda"),
    path('', views.kategori, name="kategori"),
    path('/<str:pk>/', views.produk, name="produk"),
]
