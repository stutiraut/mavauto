from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^api/v1/', include('social_django.urls', namespace='social')),


    ]
