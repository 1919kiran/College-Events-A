from django.urls import path, re_path, include
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    path('create/', views.create, name='create'),
    path('home/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.delete, name='delete'),
    re_path(r'^(?P<slug>[\w-]+)/update/$', views.update, name='update'),
    #path('events/')
]
