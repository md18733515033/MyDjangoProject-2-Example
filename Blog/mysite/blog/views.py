from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.get(id=1)
    print(posts.title)
    # for post in posts:
    #     print(post)
    #     print(post.publish)
    #     print(post.author.id)
    #     print(post.author.first_name)

        # print(1111)

    # posts.update(title="小欢喜")
    # posts_new = Post.published.all()
    # for post in posts.iterator():
    #     print(post)

    # return render(request, 'blog/post/list.html', {'posts': posts})
    return HttpResponse(content="OK")

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
