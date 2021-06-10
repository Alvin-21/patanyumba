from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import *
from .forms import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AccomodationSerializer, ProfileSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.

def index(request):
    accom = Accomodation.objects.all()
    form = SubscriptionForm()
    title = 'PataNyumba'
    return render(request, 'index.html', {"accoms": accom, "form": form})

def subscription(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    recipient = SubscriptionRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

def accomodation(request, accom_id):
    accom = Accomodation.get_accom_by_id(accom_id)
    return render(request, 'accomodation.html', {"accom": accom})

def search_results(request):
    if 'address' in request.GET and request.GET["address"]:
        search_term = request.GET.get("address")
        searched_accom = Accomodation.search_by_address(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "accoms": searched_accom})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    profile = Profile.objects.get(id=profile_id)
    accoms = Accomodation.objects.filter(user=current_user)
    return render(request, 'profile.html', {"profile": profile, "accoms": accoms})

@login_required(login_url='/accounts/login/')
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

class AccomodationList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        accoms = Accomodation.objects.all()
        serializer = AccomodationSerializer(accoms, many=True)
        return Response(serializer.data)

    