from django.urls import path

from applications.accounts.views import ActivationView, RegistrationView, LoginView, LogoutView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordCompleteView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/<str:verification_code>/', ForgotPasswordCompleteView.as_view()),
    # path('profile/<str:pk>/', ProfileView.as_view())
]