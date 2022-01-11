from django.forms import widgets
from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator
#It can only be made 150 api calls per day
#API: pruebaWebAPI104@gmail.com; PasswordWebAPI1
#API: https://api.spoonacular.com/recipes/complexSearch?apiKey=89b02dca211e450e8c3bc9361f7bbb6e&query=pizza (ALL PIZZAS)
#API: https://api.spoonacular.com/recipes/{idPizza}/information?apiKey=89b02dca211e450e8c3bc9361f7bbb6e (SET ID OF PIZZA)
#API: https://api.spoonacular.com/food/ingredients/search?query={nameIngredient}&apiKey=89b02dca211e450e8c3bc9361f7bbb6e (SET INGREDIENT NAME)
#API: https://api.spoonacular.com/food/ingredients/{idIngredient}/information?apiKey=89b02dca211e450e8c3bc9361f7bbb6e (SET ID OF INGREDIENT)

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
        return f"{self.pizzaModel.nombre}:{self.email}"

    

