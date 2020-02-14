from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    #url(r'^$', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('repair_list', views.repair_list, name='repair_list'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('repair/<int:pk>/edit/', views.repair_edit, name='repair_edit'),
    path('repair/<int:pk>/delete/', views.repair_delete, name='repair_delete'),
    path('repair/create/', views.repair_new, name='repair_new'),
    path('ticket_list', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
    path('ticket/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('ticket/create/', views.ticket_new, name='ticket_new'),
    path('map/store_location/',views.store_location, name='store_location'),
    url(r'^register/$', views.register, name='register'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]
