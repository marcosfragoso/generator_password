from django.urls import path
from app_generator_password import views

urlpatterns = [
    path('', views.home, name='home'),
    path('passwords/', views.passwords, name='list_passwords'),
]
