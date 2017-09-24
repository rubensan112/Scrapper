from django.conf.urls import include, url
from django import views

urlpatterns = [
        url(r'^$', views.post_list),
    ]