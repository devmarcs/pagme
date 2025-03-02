from django.urls import path
from . import views


urlpatterns = [
    path("cadastre-se/", views.cadastro, name="register"),
    #path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
