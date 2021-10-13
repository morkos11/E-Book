from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [

    path('signUp',views.signup_form_Page,name='signup'),
    path('signUp/complete-data',views.complete_signup,name='signup_complete'),
    path('signUp/student-data',views.student_signup,name='student_signup'),
    path('signUp/admin-data',views.admin_signup,name='admin_signup'),
    path('logIn',views.log_in,name='login'),
    path('logOut',views.log_out,name='logout'),
    path('UpdatePassword',views.change_password,name='change_password'),

    path('Reset_Password',auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset.html',success_url=reverse_lazy('accounts:password_reset_done'),email_template_name='reset_password/password_reset_email.html'),name='reset_password'),
    path('Reset_Password_Sent', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'), name='password_reset_done'),
    path('Reset_Password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/password_reset_confirm.html',success_url = reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('Reset_Password_Complete', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'), name='password_reset_complete'),

]