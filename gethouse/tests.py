from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class AccomodationTest(TestCase):
    def tearDown(self):
        Amenities.objects.all().delete()
        Accomodation.objects.all().delete()
        Profile.objects.all().delete()

    def setUp(self):
        self.pool = Amenities(name='swimming pool')
        self.pool.save()
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.property = Accomodation(user=self.user, title='trident estate', description='lovely place to live', address='Nairobi, Kenya', type_of_property='House', rent=20000, bedrooms=3, bathrooms=2, number_of_residents=2, date_available='2021-06-10', minimum_length_of_stay='1 month')
        self.property.save_accom()
        self.property.amenities.add(self.pool)

    def test_instance(self):
        self.assertTrue(isinstance(self.property, Accomodation))

    def test_save_method(self):
        accom = Accomodation.objects.all()
        self.assertTrue(len(accom) == 1)