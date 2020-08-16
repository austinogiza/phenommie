from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, ListView
from .models import Courses, SavedCourse, Lessons, UserLibrary, Reviews
from order.models import Order, OrderItem
from digi.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import ReviewForm

# Create your views here.

OWNED = 'owned'
IN_CART = 'in_cart'
NOT_IN_CART = 'not_in_cart'


def check_course_relationship(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    if course in request.user.userlibrary.course_list:
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


class CourseDetailView(DetailView):
    model = Courses
    context_object_name = 'course'
    template_name = 'coursedetails.html'

    def post(self, *args, **kwargs):
        form = ReviewForm(self.request.POST or None)
        if form.is_valid():
            course = self.get_object()
            user = self.request.user
            comment = form.cleaned_data.get('comment')
            review = Reviews(
                course=course,
                user=user,
                content=comment
            )
            review.save()
            messages.info(
                self.request, 'You are amazing!! You just left a review')
            return redirect('course:course', slug=course.slug)
        messages.info(
            self.request, 'Oh!! You didn\'t leave a review')
        return redirect('blog:blog_detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # course_status = check_course_relationship(self.request, context)
        context.update({
            'form': ReviewForm(),
            # "course_status": course_status
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        return object


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

        course_status = check_course_relationship(self.request, course_slug)

        context = {
            'object': lesson,
            # "lessons": lessons_qs[0],
            "course_status": course_status

        }

        return render(self.request, 'lessons.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
