from django.conf.urls import url
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.index, name="blog-about"),
]