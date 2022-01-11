from django.urls import include, path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('pizzas/', views.pizzas, name = 'pizzas'),
   path('pizzas/<int:pizza_id>', views.detailPizza, name='detailPizza'), #detalles de pizzas
   #path('ingredientes', views.ingredientes, name = 'ingredientes'),#search for ingredient
   path('ingredientes/<int:ingrediente_id>', views.detailIngrediente, name = 'detailIngrediente'),
   path('contacto/', views.contacto, name = 'contacto'),
   path('comentarios/', views.comentarios, name = 'comentarios'),
   path('comentario/', views.comentario, name = 'comentario'),
   path('loginORegistro/', views.loginORegistro, name = 'loginORegistro'),
   path('registro/', views.registro, name ='registro'),
   path('login/', views.loginUser, name = 'login'),
   path('myAccount/', views.myAccount, name = 'myAccount'),
   path('i18n/', include('django.conf.urls.i18n')),
]