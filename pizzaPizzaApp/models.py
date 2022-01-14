from urllib import request
from django.forms import widgets
from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# As model field:
from django_currentuser.db.models import CurrentUserField
import requests

# Create your models here.
class PizzaModel(models.Model):
    pizzaModel_id = models.IntegerField()
    nombre = models.CharField(max_length=50, default= "default")
    def __str__(self) -> str:
        return f"{self.nombre}"

class Comentario(models.Model):
    pizzaModel = models.ForeignKey(PizzaModel, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default = "default")
    descripcion = models.CharField(max_length = 2000)
    valoracion = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)]) 
    def __str__(self) -> str:
        return f"{self.pizzaModel.nombre}:{self.username}"

    

