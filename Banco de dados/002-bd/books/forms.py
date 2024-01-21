from django import forms

LIVROS_CHOICES = (
    ('R', 'Romance'),
    ('T', 'Terror'),
)

class Cad_livros(forms.Form):
    livro = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=20)
    categoria = forms.ChoiceField(choices=LIVROS_CHOICES)


