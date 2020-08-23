from django.urls import path, include

from . import views
from .views import (

    PortfolioView,
    PortfolioDetailView,

    CoursesListView
)

app_name = 'digi'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),

    path('contact-success/', views.contactsuccess, name='contactsuccess'),
    path('service/', views.service, name='service'),
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug>', PortfolioDetailView.as_view(), name='project'),
    path('portfolio/category/<slug>/',
         views.category, name='category'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('search/', views.search, name='search'),

    path('dashboard/courses', views.BoughtCourseView.as_view(),
         name='dashboard-course'),

]
