from django.contrib import admin
from django import forms
from .models import *
from django.urls import reverse,URLResolver
# Register your models here.

class PizzaModelAdmin(admin.ModelAdmin):
     list_display = ('pizzaModel_id', 'nombre')
     list_editable = ['nombre']
     search_fields = ['nombre']
     list_filter = ['nombre']
     list_per_page = 5

class ComentarioAdmin(admin.ModelAdmin):
     list_display = ('pizza_Name', 'username')
     search_fields = ['username']
     list_filter = ['username']
     list_per_page = 4

     def pizza_Name(self, obj):
         return obj.pizzaModel.nombre

     def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ComentarioAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'descripcion':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield



admin.site.register(PizzaModel, PizzaModelAdmin)
admin.site.register(Comentario, ComentarioAdmin)
