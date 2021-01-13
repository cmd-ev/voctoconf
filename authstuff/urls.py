from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

app_name = 'authstuff'
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('login/token/<str:token>', views.token_login_view, name='tokenlogin'),
    path('logout', views.logout_view, name='logout'),
    path('setname', views.setname_view, name='setname'),
]

if settings.SIGNUP_ENABLED:
    urlpatterns.append(path('register', views.register_view, name='register'))
