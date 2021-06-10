from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')