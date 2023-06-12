from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home_page'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]