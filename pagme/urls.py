from django.urls import path
from . import views

app_name = "pagme"

urlpatterns = [
    path("", views.list, name="list_debtors" ),
    path("cadastrar/", views.create, name="create_debtor"),
    path("editar_devedor/<int:pk>/", views.update, name="update_debtor"),
    path("deletar_devedor/<int:pk>/", views.delete, name="delete_debtor"),
]
