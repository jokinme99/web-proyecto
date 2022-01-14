from io import StringIO
from typing import List
from urllib.request import Request
from django.conf.urls import url
from django.shortcuts import render, redirect, get_list_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
import requests
from requests.api import get
from .forms import *
from .models import *

# If it's used 150 times change of apiKey
apiKey1 = "89b02dca211e450e8c3bc9361f7bbb6e"
apiKey2 = "27327985a7e74880934012b630350cb5"
apiKey = apiKey2


def home(request):
    data = requests.get(
        url='https://api.spoonacular.com/recipes/complexSearch?apiKey=' + apiKey + '&query=pizza')
    variable = data.json()
    pizzas = variable["results"]
    pizzaModel_list = PizzaModel.objects.all()
    if pizzaModel_list.exists() == False:
        for p in pizzas:
            pizzaModel_data = PizzaModel(
                pizzaModel_id=p['id'],
                nombre=p['title']
            )
            pizzaModel_data.save()
        all_pizzaModel = PizzaModel.objects.all().order_by('id')
    else:
        PizzaModel.objects.all().delete()
        for p in pizzas:
            pizzaModel_data = PizzaModel(
                pizzaModel_id=p['id'],
                nombre=p['title']
            )
            pizzaModel_data.save()
        all_pizzaModel = PizzaModel.objects.all().order_by('id')
    return render(request, "home.html")


def pizzas(request):
    data = requests.get(
        url='https://api.spoonacular.com/recipes/complexSearch?apiKey=' + apiKey + '&query=pizza')
    variable = data.json()
    pizzas = variable["results"]
    context = {"pizzas": pizzas}
    return render(request, "pizzas.html", context)


def detailPizza(request, pizza_id):
    data = requests.get(url="https://api.spoonacular.com/recipes/" +
                        str(pizza_id) + "/information?apiKey=" + apiKey)
    variable = data.json()
    pizza = variable
    comentariosExistingCheck_list = Comentario.objects.all()
    if comentariosExistingCheck_list.exists() == False:
        comentarios = []
    else:
        comentariosList = get_list_or_404(Comentario)
        comentarios = getList(
            comentariosList=comentariosList, pizza_id=pizza_id)
    context = {'pizza': pizza, 'comentarios': comentarios}
    return render(request, 'detailPizza.html', context)  # detail


def getList(comentariosList: List[Comentario], pizza_id: int) -> List[Comentario]:
    comentarios = []
    for e in comentariosList:
        if e.pizzaModel.pizzaModel_id == pizza_id:
            comentarios.append(e)
    return comentarios


def detailIngrediente(request, ingrediente_id):
    data = requests.get(url="https://api.spoonacular.com/food/ingredients/" +
                        str(ingrediente_id) + "/information?amount=1&apiKey=" + apiKey)
    variable = data.json()
    ingrediente = variable
    nutrition = variable["nutrition"]
    context = {'ingrediente': ingrediente, 'nutrition': nutrition}
    return render(request, 'detailIngrediente.html', context)


def contacto(request):
    return render(request, 'contacto.html')


def comentarios(request):
    data = requests.get(
        url='https://api.spoonacular.com/recipes/complexSearch?apiKey=' + apiKey + '&query=pizza')
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


def loginORegistro(request):
    return render(request, 'loginORegistro.html')


def registro(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = RegisterUser()
    return render(request, 'registro.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(
                request, 'Usuario y/o contraseña incorrectas.''\n''Revise las mayúsculas, importan! \n Puede recuperar la contraseña si no se acuerda.')
    return render(request, 'login.html')


def myAccount(request):
    data = requests.get(
        url='https://api.spoonacular.com/recipes/complexSearch?apiKey=' + apiKey + '&query=pizza')
    variable = data.json()
    pizzas = variable["results"]
    comentariosExistingCheck_list = Comentario.objects.all()
    if comentariosExistingCheck_list.exists() == False:
        comentarios = []
    else:
        comentarios = get_list_or_404(Comentario)
    context = {'comentarios': comentarios, 'pizzas': pizzas}
    return render(request, 'myAccount.html', context)


def logOutView(request):
    logout(request)
    return render(request, "home.html")
