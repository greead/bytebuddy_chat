from django.urls import path
from . import views as v


# URL Patterns for the Login app
urlpatterns = [
    path("UserprofilewithID/<int:id>/", v.UserprofilewithID, name="UserprofilewithID"),
    path('profile_list/', v.profile_list, name='profile_list'),
    
    # Sign-up page
    path('', v.startapp),
]
