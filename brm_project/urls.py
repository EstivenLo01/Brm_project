from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
from . import  views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name='login' ),
    path("", include("usuarios.urls")),
]


# @login_required
# def home(request):
#     return render(request, "home.html")


