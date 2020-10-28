from blog.models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm
from django.contrib import  messages


@require_POST
def comment(request, post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    post = get_object_or_404(Post, pk=post_pk)
    # 当获取文章（Post）存在时则获取，当获取文章不存在时，则返回404页面给用户。
    form = CommentForm(request.POST)
    # django 将用户提交的数据都封装在request.POST中，这是一个类字典对象。
    if form.is_valid():
        # 调用 form.is_valid()方法时，django会自动帮我们检查表单的数据是否符合要求。
        # 当检查到数据时合法的时候，调用表单的save方法保存数据到数据库。
        comment = form.save(commit=False)
        # commit=False 的作用时仅仅利用表格的数据生成Comment 模型类的实例，但不保存评论到数据库。
        comment.post = post
        # 将评论和被评论的文章关联起来。
        comment.save()
        # 最终将评论数据保存进数据库，调用模型实例的 save 方法
        messages.add_message(request, messages.SUCCESS, '评论发表成功!', extra_tags='success')
        return redirect(post)

    context = {
        'post': post,
        'form': form,
    }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误候从新提交。', extra_tags='danger')
    return render(request, 'comments/preview.html', context=context)
