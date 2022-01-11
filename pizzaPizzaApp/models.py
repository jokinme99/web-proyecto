from djongo import models
from django.core.validators import MaxValueValidator, MinValueValidator
#data we're going to save in the db
#pizzas and it's toppings will be only painted not saved in the db
#the db will save the 
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
    email = models.EmailField(max_length = 50)
    descripcion = models.CharField(max_length = 500)
    valoracion = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)]) 
    def __str__(self) -> str:
        return f"{self.pizzaModel.nombre}:{self.email}"

    

