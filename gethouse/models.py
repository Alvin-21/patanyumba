from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Amenities(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Accomodation(models.Model):
    PROPERTY_TYPE_VALUES = (
        ('House'),
        ('Apartment'),
    )

    LEN_OF_STAY_VALUES = (
        ('1 week'),
        ('2 weeks'),
        ('1 month'),
        ('2 months'),
        ('3 months'),
        ('4 months'),
        ('6 months'),
        ('9 months'),
        ('12 months +'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=50)
    description = models.CharField()
    address = models.CharField(max_length=150)
    type_of_property = models.CharField(choices=PROPERTY_TYPE_VALUES)
    rent = models.IntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    amenities = models.ManyToManyField(Amenities)
    number_of_residents = models.PositiveIntegerField()
    date_available = models.DateField()
    minimum_length_of_stay = models.CharField(choices=LEN_OF_STAY_VALUES)