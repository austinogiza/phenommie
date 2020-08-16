from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [

    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path('order/', views.order_view, name="order-view"),
    path('success/', views.successpayment, name="success-paystack"),
    path('failed-payment/', views.failedpayment, name="failed-paystack"),


]
