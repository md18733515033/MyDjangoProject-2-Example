from django.contrib import admin

from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status')
    # 通过包含的字段进行过滤
    list_filter = ('status', 'created', 'publish', 'author')
    # 在admin中的search查询search_fields中定义的字段
    search_fields = ('title', 'body')
    # 根据title字段输入结果填充slug字段
    prepopulated_fields = {'slug': ('title',)}
    # author字段利用搜索微件予以显示,当存在数千名用户时,其伸缩性明显优于下拉选择输入菜单
    raw_id_fields = ('author',)
    # 在search栏下方是一个导航链接,可查看日期层次结构
    date_hierarchy = 'publish'
    # 按照Status和Publish列进行排序
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'created', 'updated', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
