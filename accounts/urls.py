from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    # path('signout/', views.signout, name='signout'),
]
