from django.contrib import admin
from .models import Comment


# 创建好Comment的模型之后将其注册到 django admin的后台。
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.site.register(Comment, CommentAdmin)
