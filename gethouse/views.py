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
from rest_framework import status

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

    def post(self, request, format=None):
        serializers = AccomodationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AccomodationDetails(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_accom(self, accom_id):
        try:
            return Accomodation.objects.get(id=accom_id)
        except Accomodation.DoesNotExist:
            return Http404

    def get(self, request, accom_id, format=None):
        accom = self.get_accom(accom_id)
        serializers = AccomodationSerializer(accom)
        return Response(serializers.data)

    def put(self, request, accom_id, format=None):
        accom = self.get_accom(accom_id)
        serializers = AccomodationSerializer(accom, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, accom_id, format=None):
        accom = self.get_accom(accom_id)
        accom.delete()
        return Response({"message": "The accomodation has been successfully  deleted."}, status=status.HTTP_204_NO_CONTENT)


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetails(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_profile(self, profile_id):
        try:
            return Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, profile_id, format=None):
        profile = self.get_profile(profile_id)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)