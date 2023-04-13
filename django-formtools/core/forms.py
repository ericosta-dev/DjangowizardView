from django import forms

from core.models import Endereco, Pessoa, Time

class PessoaForm(forms.ModelForm):
    """Formulario Pessoa"""
    class Meta:
        model = Pessoa
        fields = ('nome', 'idade')

class TimeForm(forms.ModelForm):
    """Formulario Time"""
    class Meta:
        model = Time
        fields = ('nome',)

class EnderecoForm(forms.ModelForm):
    """Formulario Endereco"""
    class Meta:
        model = Endereco
        fields = ('nome', 'estado')