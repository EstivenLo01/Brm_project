from django.urls import path
from . import views

app_name = "usuarios"  # Si defines esto, usa 'usuarios:home' en el redirect

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
]
