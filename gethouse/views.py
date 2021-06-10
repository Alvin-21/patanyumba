from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    accom = Accomodation.objects.all()
    return render(request, 'index.html', {"accoms": accom})

def accomodation(request, accom_id):
    accom = Accomodation.get_accom_by_id(accom_id)
    return render(request, 'accomodation.html', {"accom": accom})

