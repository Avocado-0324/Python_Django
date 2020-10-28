from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Category是一个标准的python类，它继承了models.Model类，类名为Category。
# Category类有一个属性name，它是models.CharField 的一个实例。
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题信息
    title = models.CharField("标题", max_length=70)
    # 文章正文 TextField方法用来存储大文本
    body = models.TextField("正文")

    # 文章创建时间和最后一次修改时间
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    modified_time = models.DateTimeField("修改时间")

    # 文章摘要,因为默认情况下CharField必须存入数据，否则会报错。所以指定blank=True后就可以允许空值了。
    excerpt = models.CharField("摘要", max_length=200, blank=True)

    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True)

    # User 是从 django.contrib.auth.models 导入的
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 为了接下来点击文章或者文章下方的继续阅读可以跳转至文章内容。
    # 我们首先在urls.py设置了post的域名规则，视图函数views.detail，并命名其urls为detail
    # 接下来为了关联数据模型和urls，我们用reverse返还命名好的urls（detail）。

    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # md.convert将Markdown文本渲染成html文本
        # strip_tags 去掉HTML文本的全部HTML标签
        # 从文本中摘取前54 个字符赋给 expert
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)
