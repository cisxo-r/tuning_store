from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page,name = 'home'),
    path('about/',about,name = 'about'),
    path('catalog/',items,name = 'items'),
    path('favorite/',favorite,name = 'favorite'),
    path('office/',personal_office,name = 'office')
]
