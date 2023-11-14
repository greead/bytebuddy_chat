from django.urls import path
from . import views as v


# URL Patterns for the Login app
urlpatterns = [
    path("profile/<int:id>/", views.profile, name="profile"),
    path('profile_list/', views.profile_list, name='profile_list'),
    
    # Sign-up page
    path('', v.startapp),
]
