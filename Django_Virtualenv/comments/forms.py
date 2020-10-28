from django import forms
from .models import Comment

# django表单功能
# 首先导入 forms模块
# 创建表单的类时必须继承forms.Form/forms.ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']