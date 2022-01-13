from django.forms import widgets
from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class PizzaModel(models.Model):
    pizzaModel_id = models.IntegerField()
    nombre = models.CharField(max_length=50, default= "default")
    def __str__(self) -> str:
        return f"{self.nombre}"

class Comentario(models.Model):
    pizzaModel = models.ForeignKey(PizzaModel, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100, default="username") #The username has to exist
    descripcion = models.CharField(max_length = 2000)
    valoracion = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)]) 
    def __str__(self) -> str:
        return f"{self.pizzaModel.nombre}:{self.username}"

    

