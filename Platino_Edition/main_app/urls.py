from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('Yacht/', views.Yach, name='Yacht'),
    path('Jet/', views.jet, name='Jet'),
    path('Realstate/', views.Realstate, name='Realstate'),
    path('Car/', views.car, name='Car'),
    path('profile/', views.profile, name='profile'),
    path('addCarBooking/<int:item_id>/', views.addCarBooking, name='addCarBooking'),
    # New url pattern below
path('accounts/signup/', views.signup, name='signup'),

]
