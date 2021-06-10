from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Amenities(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Accomodation(models.Model):
    PROPERTY_TYPE_VALUES = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
    )

    LEN_OF_STAY_VALUES = (
        ('1 week', '1 week'),
        ('2 weeks', '2 weeks'),
        ('1 month', '1 month'),
        ('2 months', '2 months'),
        ('3 months', '3 months'),
        ('4 months', '4 months'),
        ('6 months', '6 months'),
        ('9 months', '9 months'),
        ('12 months +', '12 months +'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=150)
    type_of_property = models.CharField(choices=PROPERTY_TYPE_VALUES, max_length=100)
    rent = models.IntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    amenities = models.ManyToManyField(Amenities)
    number_of_residents = models.PositiveIntegerField()
    date_available = models.DateField()
    minimum_length_of_stay = models.CharField(choices=LEN_OF_STAY_VALUES, max_length=100)

    def __str__(self):
        return self.title

    def save_accom(self):
        self.save()

    def delete_accom(self):
        self.delete()

    @classmethod
    def search_by_address(cls, search_term):
        accomodation = cls.objects.filter(address__icontains=search_term)
        return accomodation

    @classmethod
    def get_accom_by_id(cls, accom_id):
        accom = cls.objects.get(id=accom_id)
        return accom
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = CloudinaryField('image', null=True)
    bio = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()