from django.urls import path
from .views import list_Agricultor, create_Agricultor, update_Agricultor, delete_Agricultor
from .views import list_Motorista, create_Motorista, update_Motorista, delete_Motorista
from .views import list_Propriedade, create_Propriedade, update_Propriedade, delete_Propriedade
from .views import list_Veiculo, create_Veiculo, update_Veiculo, delete_Veiculo
from .views import list_Endereco, create_Endereco, update_Endereco, delete_Endereco
from .views import list_Colheita, create_Colheita, update_Colheita, delete_Colheita


urlpatterns = [
    path('listAgricultor/', list_Agricultor, name='list_Agricultor'),
    path('newAgricultor/', create_Agricultor, name='create_Agricultor'),
    path('updateAgricultor/<int:id>/', update_Agricultor, name='update_Agricultor'),
    path('deleteAgricultor/<int:id>/', delete_Agricultor, name='delete_Agricultor'),
    path('listpropriedade/', list_Propriedade, name='list_Propriedade'),
    path('newPropriedade/', create_Propriedade, name='create_Proprideade'),
    path('updatePropriedade/<int:id>/', update_Propriedade, name='update_Propriedade'),
    path('deletePropriedade/<int:id>/', delete_Propriedade, name='delete_Propriedade'),
    path('listColheita/', list_Colheita, name='list_Colheita'),
    path('newColheita/', create_Colheita, name='create_Colheita'),
    path('updateColheita/<int:id>/', update_Colheita, name='update_Colheita'),
    path('deleteColheita/<int:id>/', delete_Colheita, name='delete_Colheita'),
    path('listMotorista/', list_Motorista, name='list_Motorista'),
    path('newMotorista/', create_Motorista, name='create_Motorista'),
    path('updateMotorista/<int:id>/', update_Motorista, name='update_Motorista'),
    path('deleteMotorista/<int:id>/', delete_Motorista, name='delete_Motorista'),
    path('listVeiculo/', list_Veiculo, name='list_Veiculo'),
    path('newVeiculo/', create_Veiculo, name='create_Veiculo'),
    path('updateVeiculo/<int:id>/', update_Veiculo, name='update_Veiculo'),
    path('deleteVeiculo/<int:id>/', delete_Veiculo, name='delete_Veiculo'),
    path('listEndereco/', list_Endereco, name='list_Endereco'),
    path('newEndereco/', create_Endereco, name='create_Endereco'),
    path('updateEndereco/<int:id>/', update_Endereco, name='update_Endereco'),
    path('deleteEndereco/<int:id>/', delete_Endereco, name='delete_Endereco'),
]
