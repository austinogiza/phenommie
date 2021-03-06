from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from .models import Contact, Portfolio, PortfolioCategory, CustomUser, Services, Project, Brands, Opportunities
from .forms import ContactForm, ProjectForm, OpportunityForm
from course.models import Courses
from order.models import Order, OrderItem
from course.models import SavedCourse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

OWNED = 'owned'
IN_CART = 'in_cart'
NOT_IN_CART = 'not_in_cart'


class AboutView(ListView):
    model = Services
    context_object_name = 'services'
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        brands = Brands.objects.all()
        context.update({

            'brands': brands
        })
        return context


def search(request):
    try:
        query = request.GET.get('q')
    except:
        query = None
    if query:
        results = Courses.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)).distinct()
        paginator = Paginator(results, 12)  # Show 12 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "results": results

        }
        return render(request, 'search.html', context)
    else:

        return render(request, 'search.html')
    return render(request, 'search.html')


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


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        context.update({
            "order": Order.objects.filter(user=self.request.user, is_ordered=True),
            'library': self.request.user.userlibrary.course_list,
            'count': self.request.user.userlibrary,
            'saved': SavedCourse.objects.filter(user=self.request.user),
            'orderitem': Order.objects.filter(user=self.request.user, is_ordered=False),


        })
        return context


# def dashboard(request):
#     context = {

#     }
#     return render(request, '', context)


def home(request):
    portfolio = Portfolio.objects.all()[:3]
    context = {
        'portfolio': portfolio
    }
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        return redirect('digi:contactsuccess')

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def contactsuccess(request):
    return render(request, 'contact-success.html')


class ServiceView(ListView):
    model = Services
    context_object_name = 'service'
    template_name = "services.html"


class CoursesListView(ListView):
    model = Courses
    template_name = 'courses.html'
    paginate_by = 12


class PortfolioDetailView(DetailView):
    model = Portfolio
    context_object_name = 'project'
    template_name = 'projects.html'


class PortfolioView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context.update(
            {
                'categories': PortfolioCategory.objects.all()
            }
        )
        return context


def category(request, slug):
    instance = Portfolio.objects.all()
    categories = PortfolioCategory.objects.all()
    category = get_object_or_404(PortfolioCategory, slug=slug)
    instance_qs = instance.filter(category=category)
    paginator = Paginator(instance_qs, 12)  # Show 12 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj":  page_obj,
        "category": category,
        "categories": categories

    }
    return render(request, "category.html", context)


class BoughtCourseView(LoginRequiredMixin, TemplateView):
    template_name = 'bought.html'

    def get_context_data(self, **kwargs):
        context = super(BoughtCourseView, self).get_context_data(**kwargs)

        context.update({
            "order": Order.objects.filter(user=self.request.user, is_ordered=True),
            'library': self.request.user.userlibrary.course_list,
            'count': self.request.user.userlibrary,
            'saved': SavedCourse.objects.filter(user=self.request.user),
            'orderitem': Order.objects.filter(user=self.request.user, is_ordered=False),

        })
        return context


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    template_name = "profile.html"
    fields = ['username', 'first_name', 'last_name', 'email']

    success_url = reverse_lazy('digi:profile')
    success_message = "Your profile was successfully updated"

    def get_object(self):
        return self.request.user


class ServiceSingleView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = "single.html"

    def post(self, *args, **kwargs):
        form = ProjectForm(self.request.POST or None)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            budget = form.cleaned_data.get('budget')
            company = form.cleaned_data.get('company')
            project_type = form.cleaned_data.get('project_type')
            message = form.cleaned_data.get('message')

            project = Project(
                name=name,
                email=email,
                phone=phone,
                budget=budget,
                company=company,
                project_type=project_type,
                message=message
            )
            project.save()
            return redirect('digi:contactsuccess')

    def get_context_data(self, **kwargs):
        context = super(ServiceSingleView, self).get_context_data(**kwargs)
        context.update({
            'form': ProjectForm()
        })
        return context


class OpporView(TemplateView):
    template_name = "opportunities.html"

    def post(self, *args, **kwargs):
        form = OpportunityForm(self.request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            why = form.cleaned_data.get('why')
            role = form.cleaned_data.get('role')
            links = form.cleaned_data.get('links')
            

            opportunities = Opportunities(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                why=why,
                role=role,
                links=links,
            )
            opportunities.save()
            return redirect('digi:contactsuccess')
        return render(self.request, "opportunities.html")

    def get_context_data(self, **kwargs):
        context = super(OpporView, self).get_context_data(**kwargs)
        context.update({

                'form': OpportunityForm()
            })
        return context
        
