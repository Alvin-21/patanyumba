from rest_framework import serializers
from .models import Accomodation, Profile

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = ('user', 'title', 'image', 'description', 'address', 'type_of_property', 'rent', 'bedrooms', 'bathrooms', 'amenities', 'number_of_residents', 'date_available', 'minimum_length_of_stay')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'image', 'bio', 'email', 'number')