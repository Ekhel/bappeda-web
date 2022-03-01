from django.contrib import admin
from .models import Kategori, Dokumen


class TableDokumen(admin.ModelAdmin):
    list_display = ('title', 'tgl_buat',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Kategori)
admin.site.register(Dokumen, TableDokumen)
