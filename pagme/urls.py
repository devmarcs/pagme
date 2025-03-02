from django.urls import path
from . import views

app_name = "pagme"

urlpatterns = [
    path("", views.list_people, name="peoples" ),
    path("cadastrar/", views.create, name="create_debtor"),
]
