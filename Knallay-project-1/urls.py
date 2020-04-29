from django.urls import path
from . import views

path('/contract/<int:contract_id>',views.contract, name='contract_detail'),
        # Josh contract render page 
    path('/edit_contract/<int:contract_id>',views.edit_contract),
        # Josh contract edit route