from django.urls import path
from . import views

urlpatterns = [
    path('my_orders/', views.my_orders, name='my_orders'),
    path('', views.homepage, name='homepage'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('create_order/', views.create_order, name='create_order')
]