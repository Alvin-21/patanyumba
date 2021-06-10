from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^ajax/subscription/$', views.subscription, name='subscription'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^accomodation/(\d+)', views.accomodation, name='accomodation'),
    re_path(r'^new/accomodation$', views.new_accom, name='new_accomodation'),
    re_path(r'^profile/(\d+)$', views.profile, name='profile'),
    re_path(r'^edit/profile', views.edit_profile, name='edit_profile'),
    re_path(r'^api/accomodations$', views.AccomodationList.as_view()),
    re_path(r'api/accomodation/accom-id/(\d+)$',
            views.AccomodationDetails.as_view()),
    re_path(r'^api/profiles$', views.ProfileList.as_view()),
    re_path(r'^api/profile/profile-id/(\d+)$', views.ProfileDetails.as_view()),
]
