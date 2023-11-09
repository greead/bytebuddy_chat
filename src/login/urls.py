from django.urls import path
from . import views as v


# URL Patterns for the Login app
urlpatterns = [
    # Sign-up page
    path('api/signup', v.SignupView.as_view()),
    path('api/login', v.LoginView.as_view()),
    path('api/logout', v.LogoutView.as_view()),
    path('api/csrf', v.get_csrf)
]