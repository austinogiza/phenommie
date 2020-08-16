from django.urls import path, include
from .views import (

    LessonView
)
from . import views

app_name = "course"

urlpatterns = [

    path('course/<slug>', views.course, name="course"),
    path('course/<course_slug>/<lesson_slug>/',
         LessonView.as_view(), name='lesson'),
    path('saved/<slug>/', views.saved, name='saved'),



]
