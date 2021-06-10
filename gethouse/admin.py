from django.contrib import admin
from .models import *

# Register your models here.

class AccomodationAdmin(admin.ModelAdmin):
    filter_horizontal = ('Amenities',)

admin.site.register(Profile)
admin.site.register(Accomodation, AccomodationAdmin)
admin.site.register(Amenities)