from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.shortcuts import reverse

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

    @property
    def userlibrary(self):
        return self.userlibrary_set.all()

    @property
    def courses(self):
        return self.courses_set.all()

    @property
    def course_list(self):
        return self.courses.all()

    @property
    def get_courses_saved_course(self):
        return self.savedcourse_set.all()

    @property
    def get_courses_saved_count(self):
        return self.savedcourse_set.all().count()

    @property
    def get_review_count(self):
        return self.reviews_set.all().count()


class PortfolioCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Portfolio Categories'

        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("digi:category", kwargs={"slug": self.slug})


class Portfolio(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    content_header = models.CharField(max_length=500, blank=True, null=True)
    content_body = models.TextField(max_length=2000, blank=True, null=True)
    details = models.TextField(max_length=2000, blank=True, null=True)
    presentation = models.ImageField(blank=True, null=True)
    image = models.ImageField()
    image_1 = models.ImageField(blank=True, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)
    image_4 = models.ImageField(blank=True, null=True)
    image_5 = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(
        PortfolioCategory, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("digi:project", kwargs={"slug": self.slug})
