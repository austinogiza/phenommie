from django.urls import path, include

from . import views

app_name = 'digi'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

    path('contact-success/', views.contactsuccess, name='contactsuccess'),
    path('service/', views.service, name='service'),
    path('courses/', views.courses, name='courses'),
    path('portfolio/', views.portfolio, name='portfolio'),

]
