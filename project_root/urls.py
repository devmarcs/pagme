from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pagme.urls"), name="pagme"),
    #path("", include("accounts.urls"), name="accounts"),
    #path("accounts/", include('django.contrib.auth.urls')),
]
