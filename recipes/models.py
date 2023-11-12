from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    steps = models.TextField(verbose_name='Порядок приготовления')
    time = models.PositiveIntegerField(verbose_name='Время приготовления (часы)') #в часах
    image = models.ImageField(upload_to='static/images/', verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, verbose_name='Категория блюда', through='RecipeCategory')


    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,verbose_name='Рецепт')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория блюда')