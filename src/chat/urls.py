from django.urls import path
from . import views as v


# URL Patterns for the Login app
urlpatterns = [
    path("UserprofilewithID/<int:id>/", v.UserprofilewithID, name="UserprofilewithID"),
    path('profile_list/', v.profile_list, name='profile_list'),
    path('ide/<int:chatroom_id>/', v.ide_view, name='ide_view'),
    path('image/', v.profile_view, name='profile_view'),
    # Sign-up page
    path('', v.startapp),
]
