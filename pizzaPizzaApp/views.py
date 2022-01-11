from io import StringIO
from typing import List
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import redirect
from django.utils import timezone
import requests
from requests.api import get
from .forms import *
from .models import *

def home(request):
    data = requests.get(url = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=89b02dca211e450e8c3bc9361f7bbb6e&query=pizza')
    variable = data.json()
    pizzas = variable["results"]
    pizzaModel_list = PizzaModel.objects.all()
    if pizzaModel_list.exists() == False:
        for p in pizzas:
            pizzaModel_data = PizzaModel(
            pizzaModel_id = p['id'],
            nombre = p['title']
            )
            pizzaModel_data.save()
        all_pizzaModel = PizzaModel.objects.all().order_by('id')  
    else:
        PizzaModel.objects.all().delete()
        for p in pizzas:
            pizzaModel_data = PizzaModel(
            pizzaModel_id = p['id'],
            nombre = p['title']
            )
            pizzaModel_data.save()
        all_pizzaModel = PizzaModel.objects.all().order_by('id')
    return render(request, "home.html")   

def pizzas(request):
    data = requests.get(url = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=89b02dca211e450e8c3bc9361f7bbb6e&query=pizza')
    variable = data.json()
    pizzas = variable["results"]
    context = {"pizzas": pizzas}
    return render(request, "pizzas.html", context)

def detailPizza(request, pizza_id):
    data = requests.get(url = "https://api.spoonacular.com/recipes/" + str(pizza_id) + "/information?apiKey=89b02dca211e450e8c3bc9361f7bbb6e")
    variable = data.json()
    pizza = variable
    comentariosExistingCheck_list = Comentario.objects.all()
    if comentariosExistingCheck_list.exists() == False:
        comentarios = []
    else:
     comentariosList = get_list_or_404(Comentario)
     comentarios = getList(comentariosList=comentariosList, pizza_id=pizza_id) 
    context = {'pizza': pizza, 'comentarios': comentarios}
    return render(request, 'detailPizza.html', context) #detail

def getList(comentariosList: List[Comentario], pizza_id: int) -> List[Comentario]:
	comentarios = []
	for e in comentariosList:
		if e.pizzaModel.pizzaModel_id == pizza_id:
			comentarios.append(e)
	return comentarios

#API: https://api.spoonacular.com/food/ingredients/search?query={nameIngredient}&apiKey=89b02dca211e450e8c3bc9361f7bbb6e (SET INGREDIENT NAME)
#def ingrediente(request, ingrediente_nombre):
	#data = requests.get(url = "https://api.spoonacular.com/food/ingredients/search?query=" + ingrediente_nombre + "&apiKey=89b02dca211e450e8c3bc9361f7bbb6e")
	#variable = data.json()
	#ingredientes = variable["results"]
	#context = {"ingredientes": ingredientes}
	#return render(request, "ingredientes.html", context)

def detailIngrediente(request, ingrediente_id):
	data = requests.get(url = "https://api.spoonacular.com/food/ingredients/" + str(ingrediente_id) + "/information?amount=1&apiKey=89b02dca211e450e8c3bc9361f7bbb6e")
	variable = data.json()
	ingrediente = variable
	nutrition = variable["nutrition"]
	context = {'ingrediente':ingrediente, 'nutrition': nutrition}
	return render(request, 'detailIngrediente.html', context)

def contacto(request):
	return render(request, 'contacto.html')

def comentarios(request):
 data = requests.get(url = 'https://api.spoonacular.com/recipes/complexSearch?apiKey=89b02dca211e450e8c3bc9361f7bbb6e&query=pizza')
 variable = data.json()
 pizzas = variable["results"]
 comentariosExistingCheck_list = Comentario.objects.all()
 if comentariosExistingCheck_list.exists() == False:
     comentarios = []
 else:
     comentarios = get_list_or_404(Comentario)
 context = {'comentarios': comentarios, 'pizzas': pizzas}
 return render(request, 'comentarios.html', context)


def comentario(request):
 if request.method == "POST":
     form = MyReview(request.POST)
     if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
         post.published_date = timezone.now()
         post.save()
         return redirect('comentarios')
 else:
     form = MyReview()
 return render(request, 'comentario.html', {'form': form})
