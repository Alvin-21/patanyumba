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

    def test_delete_method(self):
        self.property.delete_accom()
        accom = Accomodation.objects.all()
        self.assertTrue(len(accom) == 0)

    def test_search_accom(self):
        accom = Accomodation.search_by_address('Nairobi')
        self.assertTrue(len(accom) == 1)

    
class ProfileTest(TestCase):
    def tearDown(self):
        Amenities.objects.all().delete()
        Accomodation.objects.all().delete()
        Profile.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.prof = Profile(user=self.user, first_name='John', last_name='Doe', bio='This is a test example of my bio', email='john@test.com', number='0712345678')

    def test_instance(self):
        self.assertTrue(isinstance(self.prof, Profile))