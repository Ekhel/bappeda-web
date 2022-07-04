from django.db import models
from django.urls import reverse

import uuid

from django.forms import CharField


class Kategori(models.Model):
    kategori = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.kategori)


class Dokumen(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    kategori = models.ForeignKey(
        Kategori, on_delete=models.SET_NULL, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    tgl_produksi = models.DateField(blank=True, null=True)
    tgl_buat = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)
    file = models.FileField(null=True, blank=True)
    cover = models.ImageField(
        upload_to='dokumen_cover/', null=True, blank=True, default='dokumen/cover-default.jpeg')
    tahun = models.CharField(max_length=20, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
