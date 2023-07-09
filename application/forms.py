from django import forms

from application.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {'password':forms.PasswordInput}

class Food_blogForm(forms.ModelForm):
    class Meta:
        model =Food_blog
        fields ='__all__'