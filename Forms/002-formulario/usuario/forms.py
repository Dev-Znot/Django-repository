from django import forms

class Cadastro(forms.Form):
    username = forms.CharField(max_length=14)
    email = forms.EmailField()