from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$' , views.show_article, name='article'),
    url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', views.addlike , name='addlike'),

    ]