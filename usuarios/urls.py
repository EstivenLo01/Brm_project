from django.urls import path
from . import views

app_name = "usuarios"  # Si defines esto, usa 'usuarios:home' en el redirect

urlpatterns = [
    path("home/", views.home, name="home"),
]
