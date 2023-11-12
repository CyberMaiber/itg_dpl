
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category, RecipeCategory
from .forms import RecipeForm

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'recipes/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'recipes/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'recipes/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'recipes/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'recipes/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    context = {'recipes': recipes}
    return render(request, 'recipes/home.html', context)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipes/add_recipe.html', context)

# @login_required
# def add_recipe(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.author = request.user
#             recipe.save()
#             form.save_m2m()
#             return redirect('home')
#     else:
#         form = RecipeForm()
#     context = {'form': form}
#     return render(request, 'recipes/add_recipe.html', context)

@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'recipes/edit_recipe.html', context)


