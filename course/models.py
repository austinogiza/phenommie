from django.db import models
from digi.models import CustomUser
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save
from embed_video.fields import EmbedVideoField


class UserLibrary(models.Model):
    courses = models.ManyToManyField("Courses", blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User Library"
        verbose_name_plural = "User Library"

    def __str__(self):
        return self.user.username

    @property
    def course_list(self):
        return self.courses.all()

    @property
    def get_courses_saved_count(self):
        return self.savedcourse_set.all().count()

    @property
    def get_review_count(self):
        return self.reviews_set.all().count()


def post_user_signup_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserLibrary.objects.get_or_create(user=instance)


post_save.connect(post_user_signup_receiver, sender=settings.AUTH_USER_MODEL)


class Courses(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True, max_length=2000)
    image = models.ImageField()
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    amount = models.FloatField()
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    class Meta:
        unique_together = ('title', 'slug')
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course:course", kwargs={"slug": self.slug})

    @property
    def lessons(self):
        return self.lessons_set.all().order_by('position')

    @property
    def get_lessons_count(self):
        return self.lessons_set.all().count()

    @property
    def get_saved_count(self):
        return self.savedcourse_set.all().count()

    @property
    def get_review_count(self):
        return self.reviews_set.all().count()

    def get_saved_url(self):
        return reverse("course:saved", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("order:add-to-cart", kwargs={"slug": self.slug})


class Lessons(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True, max_length=800)
    image = models.ImageField()
    video = EmbedVideoField(blank=True, null=True)
    position = models.IntegerField()
    date_published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        unique_together = ('title', 'slug')
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course:lesson", kwargs={"course_slug": self.course.slug,
                                                "lesson_slug": self.slug, })


class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(blank=True, null=True, max_length=800)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class SavedCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Saved Course"
        verbose_name_plural = "Saved Courses"
