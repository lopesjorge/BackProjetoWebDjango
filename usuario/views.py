from django.shortcuts import render, redirect
from .models import Agricultor
from .models import Motorista
from .models import Propriedade
from .models import Colheita
from .models import Veiculo
from .models import Endereco
from .forms import AgricultorForm
from .forms import MotoristaForm
from .forms import PropriedadeForm
from .forms import ColheitaForm
from .forms import VeiculoForm
from .forms import EnderecoForm

# CRUD Agricultor


def list_Agricultor(request):
    agricultor = Agricultor.objects.all()
    return render(request, 'Agricultor.html',{'agricultor': agricultor})


def create_Agricultor(request):
    form = AgricultorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Agricultor')

    return render(request, 'AgricultorForm.html', {'form': form})


def update_Agricultor(request, id):
    agricultor = Agricultor.objects.get(id=id)
    form = AgricultorForm(request.POST or None, instance=agricultor)

    if form.is_valid():
        form.save()
        return redirect('list_Agricultor')

    return render(request, 'AgricultorForm.html', {'form': form, 'agricultor': agricultor})


def delete_Agricultor(request, id):
    agricultor = Agricultor.objects.get(id=id)

    if request.method == 'POST':
        agricultor.delete()
        return redirect('list_Agricultor')

    return render(request, 'Agricultor-delete-confirm.html', {'agricultor': agricultor})


# CRUD Propriedade


def list_Propriedade(request):
    propriedade = Propriedade.objects.all()
    return render(request, 'Propriedade.html',{'propriedade': propriedade})


def create_Propriedade(request):
    form = PropriedadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Propriedade')

    return render(request, 'PropriedadeForm.html', {'form': form})


def update_Propriedade(request, id):
    propriedade = Propriedade.objects.get(id=id)
    form = PropriedadeForm(request.POST or None, instance=propriedade)

    if form.is_valid():
        form.save()
        return redirect('list_Propriedade')

    return render(request, 'PropriedadeForm.html', {'form': form, 'propriedade': propriedade})


def delete_Propriedade(request, id):
    propriedade = Propriedade.objects.get(id=id)

    if request.method == 'POST':
        propriedade.delete()
        return redirect('list_Propriedade')

    return render(request, 'Propriedade-delete-confirm.html', {'propriedade': propriedade})


#CRUD Colheita

def list_Colheita(request):
    colheita = Colheita.objects.all()
    return render(request, 'Colheita.html',{'colheita': colheita})


def create_Colheita(request):
    form = ColheitaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Colheita')

    return render(request, 'ColheitaForm.html', {'form': form})


def update_Colheita(request, id):
    colheita = Colheita.objects.get(id=id)
    form = ColheitaForm(request.POST or None, instance=colheita)

    if form.is_valid():
        form.save()
        return redirect('list_Colehita')

    return render(request, 'ColheitaForm.html', {'form': form, 'colheita': colheita})


def delete_Colheita(request, id):
    colheita = Colheita.objects.get(id=id)

    if request.method == 'POST':
        colheita.delete()
        return redirect('list_Colheita')

    return render(request, 'Colheita-delete-confirm.html', {'colheita': colheita})


#CRUD Motorista

def list_Motorista(request):
    motorista = Motorista.objects.all()
    return render(request, 'Motorista.html',{'motorista': motorista})


def create_Motorista(request):
    form = MotoristaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Motorista')

    return render(request, 'MotoristaForm.html', {'form': form})


def update_Motorista(request, id):
    motorista = Motorista.objects.get(id=id)
    form = MotoristaForm(request.POST or None, instance=motorista)

    if form.is_valid():
        form.save()
        return redirect('list_Motorista')

    return render(request, 'MotoristaForm.html', {'form': form, 'motorista': motorista})


def delete_Motorista(request, id):
    motorista = Motorista.objects.get(id=id)

    if request.method == 'POST':
        motorista.delete()
        return redirect('list_Motorista')

    return render(request, 'Motorista-delete-confirm.html', {'motorista': motorista})

#CRUD Veiculo

def list_Veiculo(request):
    veiculo = Veiculo.objects.all()
    return render(request, 'Veiculo.html',{'veiculo': veiculo})


def create_Veiculo(request):
    form = VeiculoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Veiculo')

    return render(request, 'VeiculoForm.html', {'form': form})


def update_Veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)

    if form.is_valid():
        form.save()
        return redirect('list_Veiculo')

    return render(request, 'VeiculoForm.html', {'form': form, 'veiculo': veiculo})


def delete_Veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('list_Veiculo')

    return render(request, 'Veiculo-delete-confirm.html', {'veiculo': veiculo})

#CRUD Endereço


def list_Endereco(request):
    endereco = Endereco.objects.all()
    return render(request, 'Endereco.html',{'endereço': endereco})


def create_Endereco(request):
    form = EnderecoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_Endereco')

    return render(request, 'EnderecoForm.html', {'form': form})


def update_Endereco(request, id):
    endereco = Endereco.objects.get(id=id)
    form = EnderecoForm(request.POST or None, instance=endereco)

    if form.is_valid():
        form.save()
        return redirect('list_Endereco')

    return render(request, 'EnderecoForm.html', {'form': form, 'endereco': endereco})


def delete_Endereco(request, id):
    endereco = Endereco.objects.get(id=id)

    if request.method == 'POST':
        endereco.delete()
        return redirect('list_Endereco')

    return render(request, 'Endereco-delete-confirm.html', {'endereco': endereco})
