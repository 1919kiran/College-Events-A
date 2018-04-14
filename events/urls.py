from django.urls import path, re_path, include
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('home/', views.index, name='home'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.delete, name='delete'),
    re_path(r'^(?P<slug>[\w-]+)/update/$', views.update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/view_participants/$', views.view_participants, name='view_participants'),
    #path('events/')
]
