from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('post/', views.post_new, name='post_new'),
    url(r'^$', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]