from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
from . import  views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name='login' ),
    path("user/", include("usuarios.urls")),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_completo/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


# @login_required
# def home(request):
#     return render(request, "home.html")


