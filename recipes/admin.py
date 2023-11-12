from django.contrib import admin
from .models import Category, Recipe, RecipeCategory

# Register your models here.

class CategoryAdminView(admin.ModelAdmin):
    list_display = ['name','description']


class RecipeAdminView(admin.ModelAdmin):
    list_display = ['title','author']


class RecipeCategoryAdminView(admin.ModelAdmin):
    list_display = ['recipe','category']



admin.site.register(Category, CategoryAdminView)
admin.site.register(Recipe, RecipeAdminView)
admin.site.register(RecipeCategory, RecipeCategoryAdminView)