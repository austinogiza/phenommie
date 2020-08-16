from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Contact, Portfolio, PortfolioCategory
from .forms import ContactForm
from course.models import Courses

# Create your views here.


def home(request):
    return render(request, 'index.html')


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


def service(request):
    return render(request, 'services.html')


class CoursesListView(ListView):
    model = Courses
    template_name = 'courses.html'
    paginate_by = 12


class PortfolioDetailView(DetailView):
    model = Portfolio
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


class PortfolioCategoryView(ListView):
    model = PortfolioCategory
    template_name = 'category.html'

    def get_queryset(self):
        qs = Portfolio.objects.all()
        category = self.request.GET.get('category', None)
        if category:
            qs = qs.filter(category__title=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PortfolioCategoryView, self).get_context_data(**kwargs)
        context.update(
            {
                'categories': PortfolioCategory.objects.all()
            }
        )
        return context
