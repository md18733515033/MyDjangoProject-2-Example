from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250, default="", verbose_name="帖子标题", help_text="帖子标题")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, verbose_name="发帖人", help_text="发帖人", on_delete=models.CASCADE,
                               related_name="blog_posts")
    body = models.TextField(verbose_name="帖子内容", help_text="帖子内容", default="")
    publish = models.DateTimeField(default=timezone.now, verbose_name="帖子发布日期", help_text="帖子发布日期")
    created = models.DateTimeField(auto_now_add=True, verbose_name="帖子创建日期", help_text="帖子创建日期")
    updated = models.DateTimeField(auto_now=True, verbose_name="帖子更新日期", help_text="帖子更新日期")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name="帖子状态",
                              help_text="帖子状态")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
