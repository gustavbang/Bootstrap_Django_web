from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('overview', views.overview, name='overview'),
    path('test', views.test, name='test'),
    path('login', views.login, name='login'),
    path('loggedin', views.loggedin, name='loggedin')
]