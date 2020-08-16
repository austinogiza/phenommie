from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from course.models import Courses
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_to_cart(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    order_item = OrderItem.objects.create(course=course)
    order, created = Order.objects.get_or_create(user=request.user)
    order.items.add(order_item)
    order.save()
    return redirect('order:order-view')


def order_view(request):
    order = get_object_or_404(Order, user=request.user)
    email = request.user.email
    amount = order.get_total()
    context = {
        'order': order,
        'amount': amount,
        "email": email
    }

    return render(request, 'order.html', context)


def successpayment(request):
    order = Order.objects.get(
        user=request.user, is_ordered=True)
    context = {
        'order': order
    }
    return render(request, 'success.html', context)


def failedpayment(request):
    return render(request, 'failed.html')
