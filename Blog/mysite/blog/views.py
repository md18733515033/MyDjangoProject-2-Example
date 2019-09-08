from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    objects_list = Post.published.all()
    paginator = Paginator(objects_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = Post.objects.get(slug=post, status='published', publish__year=year)
    return render(request, 'blog/post/detail.html', {'post': post})


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'
