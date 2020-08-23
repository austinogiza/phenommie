from django.db import models
from course.models import Courses
from django.conf import settings
from django.db.models import Sum

# Create your models here.


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.course.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ref_code = models.CharField(max_length=200, blank=True, null=True)
    payment = models.ForeignKey(
        "Payment", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ('ref_code',)

    def __str__(self):
        return self.user.username

    def get_total(self):
        return self.items.all().aggregate(order_total=Sum('course__amount'))['order_total']


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL, blank=True, null=True)
    # order = models.ForeignKey(
    #     Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_paid = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length=200, blank=True, null=True)
    total = models.FloatField()

    def __str__(self):
        return self.user.username
