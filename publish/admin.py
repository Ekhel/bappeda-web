from django.contrib import admin
from .models import Kategori, Dokumen


class TableDokumen(admin.ModelAdmin):
    list_display = ('title', 'tgl_buat', 'tahapan', 'tahun',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('kategori',)
    list_per_page = 10


admin.site.register(Kategori)
admin.site.register(Dokumen, TableDokumen)
