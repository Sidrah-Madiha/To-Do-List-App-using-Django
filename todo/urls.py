"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from todolist.views import list_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	# path('', admin.site.urls), # password:Click123
    path('admin/', admin.site.urls),
    # path('todolist/', list_view, name='home'),
    path('todolist/', include('todolist.urls', namespace='todolist')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('', include('todolist.urls')),
    path('', signup, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('accounts.urls')),
    path('reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
    path('reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    # 
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
]



