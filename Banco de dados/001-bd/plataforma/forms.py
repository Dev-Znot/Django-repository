from django import forms # Crio um arquivo dentro do app -> 'forms.py' e importo forms

class cliente(forms.Form): # Cria-se o forms
    nome = forms.CharField(max_length=20)
    data_nacimento = forms.DateField()
    email = forms.EmailField(required=False)
    descricao = forms.CharField(max_length=100, required=False)