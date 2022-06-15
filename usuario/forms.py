from dataclasses import field, fields
from django import forms
from .models import Agricultor
from .models import Colheita
from .models import Endereco
from .models import Motorista
from .models import Propriedade
from .models import Veiculo


class AgricultorForm(forms.ModelForm):
    class Meta:
        model = Agricultor
        fields = ['Nome', 'CPF', 'Telefone']


class ColheitaForm(forms.ModelForm):
    class Meta:
        model = Colheita
        fields = ['Tipo', 'Quantidade', 'AnoDaColheita']


class PropriedadeForm(forms.ModelForm):
    class Meta:
        model = Propriedade
        fields = ['Nome', 'Proprietario', 'Area']


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['Nome', 'Matricula', 'CNH', 'Categoria']


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['Modelo', 'Marca', 'AnoDeFabricacao']


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['CEP', 'Cidade', 'Bairro', 'Rua', 'Numero']
