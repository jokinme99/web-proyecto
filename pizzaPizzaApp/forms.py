from email.policy import default
from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class MyReview(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(MyReview, self).__init__(*args, **kwargs)
        self.fields['pizzaModel'] = forms.ModelChoiceField(queryset= PizzaModel.objects.all())
        self.fields['username'] = forms.CharField(max_length=50)
        self.fields['descripcion'] = forms.CharField(
            max_length = 2000,
            widget = forms.Textarea()
        )
        self.fields['valoracion'] = forms.IntegerField()
    class Meta:
        model = Comentario
        fields = ('pizzaModel', 'username', 'descripcion', 'valoracion')
class RegisterUser(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


