from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class amenities(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name