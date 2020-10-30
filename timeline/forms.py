from django import forms


class CriarPostagemForm(forms.Form):
    nome_postagem = forms.CharField(max_length=255, required=True)
    texto = forms.CharField(required=True)
