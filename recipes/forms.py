from .models import Recipe, Category
from django import forms

class RecipeForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'time', 'image', 'categories']
