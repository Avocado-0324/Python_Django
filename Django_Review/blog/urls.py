from django.urls import path
from . import views

# urlpatterns 网址和处理函数的关系。第一个参数：网址 第二个参数：处理函数 第三个参数：name（作为处理函数index的别名）
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
