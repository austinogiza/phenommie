from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, ListView
from .models import Courses, SavedCourse, Lessons, UserLibrary
from order.models import Order, OrderItem
from digi.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

OWNED = 'owned'
IN_CART = 'in_cart'
NOT_IN_CART = 'not_in_cart'


def check_course_relationship(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    if course in request.user.userlibrary.courses.all():
        return OWNED
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = OrderItem.objects.filter(course=course)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                return IN_CART
    return NOT_IN_CART


# @login_required
def course(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    # course_status = check_course_relationship(request, course)
    context = {
        # 'course_status': course_status,
        'course': course
    }
    return render(request, "coursedetails.html", context)


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Courses
    context_object_name = 'course'
    template_name = 'coursedetails.html'

    def get(self, request, *args, **kwargs):
        course_status = check_course_relationship(
            self.request, self.get_object())

    def get_object(self, **kwargs):
        context = super().get_object(**kwargs)
        return context


def saved(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    saved_qs = SavedCourse.objects.filter(user=request.user, course=course)
    if saved_qs.exists():
        saved_qs[0].delete()
        messages.info(request, 'Course removed from your saved list')

        return redirect('course:course', slug=slug)
    SavedCourse.objects.create(user=request.user, course=course)
    messages.info(request, 'Course added to your saved list')
    return redirect('course:course', slug=slug)


class LessonView(LoginRequiredMixin, View):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Courses.objects.filter(slug=course_slug)

        # lessons_qs = Lessons.objects.filter(
        #     course__slug=course_slug).filter(course__lessons__slug=lesson_slug)

        if course_qs.exists():
            course = course_qs.first()

        lessons_qs = course.lessons.filter(slug=lesson_slug)
        if lessons_qs.exists():
            lesson = lessons_qs.first()

        context = {
            'object': lesson,
            # "lessons": lessons_qs[0],

        }

        return render(self.request, 'lessons.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
