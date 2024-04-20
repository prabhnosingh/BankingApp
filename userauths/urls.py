from django.urls import path
from userauths import views
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

app_name = 'userauths'

urlpatterns = [
    path("sign-up/", views.RegisterView, name="sign-up"),
    path("sign-in/", views.LoginView, name="sign-in"),
    path("login/", views.LoginView, name="sign-in"),
    path("sign-out/", views.logoutView, name="sign-out"),
    path("password_reset_confirm/", views.password_reset_confirm, name="password_reset_confirm"),
    path("delete_account/", views.delete_account, name="delete_account"),
# path("password_reset_confirm/", views.password_reset_confirm, name="password_reset_confirm"),
    path("delete_account/", views.delete_account, name="delete_account"),
    path('password_reset_form/', PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view() , name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='userauths/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]