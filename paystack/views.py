import json
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from django.views.generic import RedirectView, TemplateView
# Create your views here.
from . import settings, signals, utils
from paystack.signals import payment_verified
from .utils import load_lib
from django.dispatch import receiver
import random
import string
from order.models import Order, OrderItem, Payment


def create_ref_code():
    ''.join(random.choices(string.digits, k=6))


def verify_payment(request, order):
    amount = request.GET.get('amount')
    txrf = request.GET.get('trxref')
    PaystackAPI = load_lib()
    paystack_instance = PaystackAPI()
    response = paystack_instance.verify_payment(txrf, amount=int(amount))
    if response[0]:
        payment_verified.send(
            request=request,
            sender=PaystackAPI,
            ref=txrf,
            amount=int(amount) / 100,
            order=order)
        return redirect("order:success-paystack")
    return redirect("order:failed-paystack")


@receiver(payment_verified)
def on_payment_verified(request, sender, ref, amount, **kwargs):
    order = Order.objects.get(user=request.user, is_ordered=False)
    user = request.user
    ref_code = create_ref_code()

    order.ref_code = ref_code
    order.is_ordered = True
    order.user = request.user
    payment = Payment()
    payment.user = request.user
    payment.total = amount
    payment.ref = ref
    payment.save()

    order_items = order.items.all()
    order_items.update(is_ordered=True)
    for item in order_items:
        courses = [item.course for item in order_items]
        item.save()
        for course in courses:
            request.user.userlibrary.courses.add(course)
    order.payment = payment
    order.save()


class FailedView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        if settings.PAYSTACK_FAILED_URL == 'paystack:failed_page':
            return reverse(settings.PAYSTACK_FAILED_URL)
        return settings.PAYSTACK_FAILED_URL


def success_redirect_view(request, order_id):
    url = settings.PAYSTACK_SUCCESS_URL
    if url == 'paystack:success_page':
        url = reverse(url)
    return redirect(url, permanent=True)


def failure_redirect_view(request, order_id):
    url = settings.PAYSTACK_FAILED_URL
    if url == 'paystack:failed_page':
        url = reverse(url)
    return redirect(url, permanent=True)


class SuccessView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        if settings.PAYSTACK_SUCCESS_URL == 'paystack:success_page':
            return reverse(settings.PAYSTACK_SUCCESS_URL)
        return settings.PAYSTACK_SUCCESS_URL


def webhook_view(request):
    # ensure that all parameters are in the bytes representation
    PaystackAPI = load_lib()
    paystack_instance = PaystackAPI()
    signature = request.META['HTTP_X_PAYSTACK_SIGNATURE']
    paystack_instance.webhook_api.verify(
        signature, request.body, full_auth=True)
    # digest = utils.generate_digest(request.body)
    # if digest == signature:
    #     payload = json.loads(request.body)
    #     signals.event_signal.send(
    #         sender=request, event=payload['event'], data=payload['data'])
    return JsonResponse({'status': "Success"})
