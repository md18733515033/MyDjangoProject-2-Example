from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManger(models.Manager):
    def get_queryset(self):
        return super(PublishedManger, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250, default="", verbose_name="帖子标题", help_text="帖子标题")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, verbose_name="发帖人", help_text="发帖人", on_delete=models.CASCADE,
                               related_name="posts")
    body = models.TextField(verbose_name="帖子内容", help_text="帖子内容", default="")
    publish = models.DateTimeField(default=timezone.now, verbose_name="帖子发布日期", help_text="帖子发布日期")
    created = models.DateTimeField(auto_now_add=True, verbose_name="帖子创建日期", help_text="帖子创建日期")
    updated = models.DateTimeField(auto_now=True, verbose_name="帖子更新日期", help_text="帖子更新日期")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name="帖子状态",
                              help_text="帖子状态")
    objects = models.Manager()
    published = PublishedManger()


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """可以使用模板中的get_absolute_url()方法,进而链接至特定的帖子"""
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
