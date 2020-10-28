from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = 'comments'
    verbose_name = "评论"  # 让comments应用在admin后台显示中文。
