from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post, PostLike, PostComment
from django.contrib import messages
from .forms import CommentForm
# Create your views here.


class BlogListView(ListView):
    model = Post
    paginate_by = 12
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            post = self.get_object()
            user = self.request.user
            comment = PostComment(
                content=content,
                user=user,
                post=post
            )
            comment.save()
            messages.info(
                self.request, 'You are amazing!! You just left a comment')
            return redirect('blog:blog_detail', slug=post.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        return object


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = PostLike.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        messages.info(request, "Oh No! You unliked the post")

        return redirect('blog:blog_detail', slug=slug)
    messages.info(request, "YAYYYY! You liked the post")
    PostLike.objects.create(user=request.user, post=post)
    return redirect('blog:blog_detail', slug=slug)
