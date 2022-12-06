from django.shortcuts import render, redirect
from .models import Car, Realestate, Yacht, Jet, User

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# ...


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
 return render(request,'home.html')

def about(request):
 return render(request,'about.html')

def profile(request):
 return render(request,'profile.html')


def Realstate(request):
    real = Realestate.objects.all()
    for r in real:
        r = r.multimg_set.all()
        print(r)
    return render(request, 'Realstate.html', {'real': real})

def Yach(request):
    boat = Yacht.objects.all()
    for yay in boat:
        yay = yay.multimg_set.all()
        print(yay)
    return render(request, 'Yacht.html', {'boat':boat})

def car(request):
    # vehicle = Car.objects.all()
    vehicle = Car.objects.all()
    for v in vehicle:
        v = v.multimg_set.all()
        print(v)
    return render(request, 'Car.html', {'vehicle':vehicle})


def jet(request):
    je = Jet.objects.all()
    for j in je:
        j = j.multimg_set.all()
        print(j)
    return render(request, 'Jet.html', {'je':je})






