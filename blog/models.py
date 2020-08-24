from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,  blank=True, null=True)
    thumbnail = models.ImageField()
    content = RichTextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})

    def get_like_url(self):
        return reverse("blog:like", kwargs={"slug": self.slug})

    @property
    def comments(self):
        return self.postcomment_set.all()

    @property
    def get_comment_count(self):
        return self.postcomment_set.all().count()

    @property
    def get_like_count(self):
        return self.postlike_set.all().count()


class PostComment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=5500, blank=True, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    publish_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


class PostLike(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
