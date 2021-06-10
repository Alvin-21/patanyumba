from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    accom = Accomodation.objects.all()
    return render(request, 'index.html', {"accoms": accom})

def accomodation(request, accom_id):
    accom = Accomodation.get_accom_by_id(accom_id)
    return render(request, 'accomodation.html', {"accom": accom})

def new_accom(request):
    current_user = request.user

    if request.method == 'POST':
        form = AccomodationForm(request.POST, request.FILES)
        if form.is_valid:
            accom = form.save(commit=False)
            accom.user = current_user
            accom.save()
        return redirect('homepage')  
    else:
        form = AccomodationForm()

    return render(request, 'new_accomodation.html', {'form': form})

def profile(request, profile_id):
    current_user = request.user
    profile = Profile.objects.get(id=profile_id)
    accoms = Accomodation.objects.filter(user=current_user)
    return render(request, 'profile.html', {"profile": profile, "accoms": accoms})

def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')
    else:
        form = ProfileForm()

    return render(request, 'edit_profile.html', {"form": form})