from django.urls import path
from . import views as v


# URL Patterns for the Login app
urlpatterns = [
    # Sign-up page
    path('', v.startapp),
]
