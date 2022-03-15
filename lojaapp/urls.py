from constantly import NamedConstant
from django.urls import path,include
from .views import *


app_name = "lojaapp"

urlpatterns = [
    path("sobre/",SobreView.as_view(), name="sobre"),
    path("contato/",ContatoView.as_view(), name="contato"),
    path("pagamento/",PagamentoView.as_view(),name="pagamento")
]