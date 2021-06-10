from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^ajax/subscription/$', views.subscription, name='subscription'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^accomodation/(\d+)', views.accomodation, name='accomodation'),
    re_path(r'^new/accomodation$', views.new_accom, name='new_accomodation'),
]