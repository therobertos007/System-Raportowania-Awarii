"""Definiuje wzorce dla adresów URL dla aplikacji users."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
	# Strona logowania.
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),

    # Strona wylogowania.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Strona rejestracji
    path('register/', views.register, name='register')
]
