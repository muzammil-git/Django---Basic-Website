from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout')
]