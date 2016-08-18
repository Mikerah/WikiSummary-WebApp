from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article.html/', views.article, name='article'),
    url(r'^articles.html/', views.articles, name='articles')
]