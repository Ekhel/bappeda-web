from django.contrib import admin
from .models import Article


class TableArticle(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_date',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, TableArticle)
