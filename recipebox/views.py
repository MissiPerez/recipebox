from django.shortcuts import render
from recipebox.models import RecipeTitle, Author 


def index(request, *args, **kwargs):

    html = 'hello.html'
    items = RecipeTitle.objects.all()
    return render(request, html, {'recipes': items})


def recipe_info(request, id):
    html = 'recipes.html'
    items = RecipeTitle.objects.all()
    instructions = items[0].instructions.split("/n")
    return render(request, html, {'recipes': items, "instructions": instructions})
    

def authordetails(request, id):
    html = 'authordetails.html'
    authors = Author.objects.all()
    items = RecipeTitle.objects.all()
    return render(request, html, {'recipes': items, "authors": authors})

