from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import SignupView

# router = DefaultRouter()
# router.register(r"signup",SignupView,basename="SignUp")

urlpatterns = [
    path('api/signup',SignupView.as_view()),
]