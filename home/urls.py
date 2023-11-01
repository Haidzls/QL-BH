from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHome, name='home'),
    path('manage/', views.getManage, name='manage'),
    path('add/', views.getAdd, name='add'),
    path('order/', views.getOrder, name='order'),
]