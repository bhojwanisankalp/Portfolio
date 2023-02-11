from django.urls import path

from . import views

#Urls patterns for /api End point
urlpatterns = [
    path('users', views.users),
    path('submit-contact', views.submit_contact)
]