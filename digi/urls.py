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
    path('service/', views.ServiceView.as_view(), name='service'),
    path('service/<slug>', views.ServiceSingleView.as_view(), name='single'),
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug>', PortfolioDetailView.as_view(), name='project'),
    path('portfolio/category/<slug>/',
         views.category, name='category'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('search/', views.search, name='search'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('dashboard/courses', views.BoughtCourseView.as_view(),
         name='dashboard-course'),
    path('dashboard/profile/', views.ProfileView.as_view(),
         name='profile'),
    path('opportunities/', views.OpporView.as_view(), name='opportunities')

]
