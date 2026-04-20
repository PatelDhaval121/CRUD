from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('register/', views.registerform, name='register'),
    path('contact/', views.contact, name='contact'),
    path('contactlist/', views.contactlist, name='contactlist'),
]