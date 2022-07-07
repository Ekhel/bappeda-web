from django.contrib import admin
from .models import Article, Topik


class TableArticle(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_date',)
    prepopulated_fields = {'slug': ('title',)}


class TableTopik(admin.ModelAdmin):
    list_display = ('top',)
    prepopulated_fields = {'slug': ('top',)}


admin.site.register(Article, TableArticle)
admin.site.register(Topik, TableTopik)
