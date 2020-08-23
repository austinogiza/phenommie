from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from course.models import Courses
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def add_to_cart(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        course=course,
        user=request.user,
        is_ordered=False)
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(course__slug=course.slug).exists():
            return redirect('order:order-view')
        else:
            order.items.add(order_item)
            order.save()
            return redirect('order:order-view')
    order = Order.objects.create(user=request.user)
    order.items.add(order_item)
    order.save()
    return redirect('order:order-view')


@login_required
def order_view(request):
    order = get_object_or_404(Order, user=request.user, is_ordered=False)
    email = request.user.email
    amount = order.get_total()
    context = {
        'order': order,
        'amount': amount,
        "email": email
    }
    if order:
        return render(request, 'order.html', context)
    else:
        messages.info(
            self.request, 'You currently have no course in your order')
        return('course:course')
    return render(request, 'order.html', context)


@login_required
def successpayment(request):
    context = {

    }
    return render(request, 'success.html', context)


@login_required
def failedpayment(request):
    return render(request, 'failed.html')
