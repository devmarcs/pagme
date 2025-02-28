from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("cadastre-se/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
