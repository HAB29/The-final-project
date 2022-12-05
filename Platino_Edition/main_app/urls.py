from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('Yacht/', views.Yacht, name='Yacht'),
    path('Jet/', views.Jet, name='Jet'),
    path('Realstate/', views.Realstate, name='Realstate'),
    path('Car/', views.Car, name='Car'),

    # New url pattern below
path('accounts/signup/', views.signup, name='signup'),

]
