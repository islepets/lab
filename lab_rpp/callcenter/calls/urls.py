# urls.py (updated)
from django.urls import path
from . import views

urlpatterns = [
    # Calls
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.home, name='home'),

    path('calls/', views.call_list, name='call_list'),
    path('calls/add/', views.call_create, name='call_create'),
    path('calls/edit/<int:pk>/', views.call_update, name='call_update'),
    path('calls/delete/<int:pk>/', views.call_delete, name='call_delete'),

    # Clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'),
    path('clients/edit/<int:pk>/', views.client_update, name='client_update'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),

    # Reasons
    path('reasons/', views.reason_list, name='reason_list'),
    path('reasons/add/', views.reason_create, name='reason_create'),
    path('reasons/edit/<int:pk>/', views.reason_update, name='reason_update'),
    path('reasons/delete/<int:pk>/', views.reason_delete, name='reason_delete'),

    # Operators
    path('operators/', views.operator_list, name='operator_list'),
    path('operators/add/', views.operator_create, name='operator_create'),
    path('operators/edit/<int:pk>/', views.operator_update, name='operator_update'),
    path('operators/delete/<int:pk>/', views.operator_delete, name='operator_delete'),

    # Statuses
    path('statuses/', views.status_list, name='status_list'),
    path('statuses/add/', views.status_create, name='status_create'),
    path('statuses/edit/<int:pk>/', views.status_update, name='status_update'),
    path('statuses/delete/<int:pk>/', views.status_delete, name='status_delete'),
]