from django.urls import path
from .views import *

#
urlpatterns = [
    path('', home, name = 'homepage'),
    path('other/', other, name = 'otherpage'),
   path('about/', about, name = 'about'),
   path('cgpa/', cgpa, name = 'cgpa'),
   path('gpa/', gpa, name = 'gpa'),
   path('portfolio/', portfolio, name = 'portfolio'),
   path('service/', service, name = 'service'),
   path('contact/', contact, name = 'contact'),
   path('add/', add, name = 'add'),
]
