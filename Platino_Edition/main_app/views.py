from django.shortcuts import render, redirect
from .models import *

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


def addCarBooking(request, item_id):
    c = Car.objects.get(id=item_id)
    b = request.user.booking_set.create(cars=c)
    b.save()
    return redirect('profile')

def removeBooking(request, item_id, item_name):
    if item_name == 'cars':
        b = Booking.objects.get(id=item_id)
        request.user.booking_set.remove(b)

    elif item_name == 'realestates':
        z = Booking.objects.get(id=item_id)
        request.user.booking_set.remove(z)
            
    elif item_name == 'jets':
        y = Booking.objects.get(id=item_id)
        request.user.booking_set.remove(y)
            
    elif item_name == 'yachts':
        x = Booking.objects.get(id=item_id)
        request.user.booking_set.remove(x)

    return redirect('profile')

def addRealBooking(request, item_id):
    re = Realestate.objects.get(id=item_id)
    rea = request.user.booking_set.create(realestates=re)
    rea.save()
    return redirect('profile')

def addJetBooking(request, item_id):
    jey = Jet.objects.get(id=item_id)
    jea = request.user.booking_set.create(jets=jey)
    jea.save()
    return redirect('profile')

def addYachtBooking(request, item_id):
    yachy = Yacht.objects.get(id=item_id)
    yea = request.user.booking_set.create(yachts=yachy)
    yea.save()
    return redirect('profile')



