# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL within the users app
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
