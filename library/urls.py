from django.contrib import admin
from django.urls import path, include
from .views import views, auth

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path("profile/", views.profile, name="profile"),
    path("choice/", views.choice, name="choice"),
    
    path("login/", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
    path("register/", auth.register, name="register"),
]
