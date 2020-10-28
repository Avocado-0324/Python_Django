from django.urls import path
from . import views

#命名空间，用来告诉django这个urls。py模块是属于blog应用的，以防止于其他视图函数冲突。
app_name = 'blog'

# 绑定网址和对应函数。
# 给path传入两三个参数，网址，参数处理函数以及name做为处理函数index的别名。
urlpatterns = [
    path('', views.index, name='index'),
#定义域名，例：post/1/代表第一篇文章。 <ink:pk> 是django路由规则的特殊写法，
#其作用是从用户访问的URL离把匹配的数字捕获并作为关键参数传给其对应的视图函数detail。
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
