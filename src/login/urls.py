from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import SignupView


# URL Patterns for the Login app
urlpatterns = [
    # Sign-up page
    path('api/signup', SignupView.as_view()),
]