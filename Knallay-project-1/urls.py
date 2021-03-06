from django.urls import path
from . import views

urlpatterns = [
    path("/contract/<int:contract_id>", views.contract, name="contract_detail"),
            # GET -> render contract.html

        path('/edit_contract/<int:contract_id>',views.edit_contract),
            # Josh contract edit route
        path('/archive_contract/<int:contract_id>',views.archive_contract),
        path('/contract_comment/<int:contract_id>',views.contract_comment),
]