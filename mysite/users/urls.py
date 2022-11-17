from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView


app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('signup/', include('django.contrib.auth.urls')),
    #path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    ]