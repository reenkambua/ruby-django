from django.urls import path
from pioneer import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('blogs/',views.blog,name='blogs'),
]