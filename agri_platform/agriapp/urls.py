from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name='logout'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms and conditions')
]
