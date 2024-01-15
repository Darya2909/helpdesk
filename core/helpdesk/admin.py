from django.contrib import admin
from .models import Article
from .models import Category
from mptt.admin import MPTTModelAdmin
from django import forms


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
