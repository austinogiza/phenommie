from django.urls import path, include
from . import views
from .views import (

    BlogListView,
    BlogDetailView
)
app_name = 'blog'

urlpatterns = [

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('like/<slug>', views.like, name='like'),

]
