from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    #url(r'^api/v1/', include('social_django.urls', namespace='social')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('crm:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('crm:password_reset_done')), {'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('crm:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    ]
