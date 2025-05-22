from django.urls import path
from . import views

urlpatterns = [
    path('', views.call_list, name='call_list'),
    path('add/', views.call_create, name='call_create'),
    path('edit/<int:pk>/', views.call_update, name='call_update'),
    path('delete/<int:pk>/', views.call_delete, name='call_delete'),
]