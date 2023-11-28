import json

from django.contrib.auth import authenticate, login, logout, models
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.db import IntegrityError
from chat.models import Profile

@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.', 'sessionid':request.session.session_key, 'userid':user.id})

@require_POST
def signup_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
         return JsonResponse({'detail': 'Please provide username and password.'}, status=400)
    
    try:
        user = models.User.objects.create_user(
                username = username,
                password = password,
                email=  username)
        # Split username(email) and use first portion as displayname
        profile = Profile(user= user, display_name =username.split("@")[0])
        user.save()
        profile.save()

    except IntegrityError as e:
            return JsonResponse({'detail': 'Please enter a different email!'}, status = 400)
 
    #extra
    # login(request, user)
    return JsonResponse({'detail':'Successfully registered'})

@ensure_csrf_cookie
def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True, 'sessionid':request.session.session_key})

#TO-DO:
#make a view to return profile picture

#In-progress:
# profile pictures is stored in media/images using ImageField
# so I created a media/images at the project directory (don't know if it is correct)
# pfp will be return as a url based on user id
# svelte will using url to serve
#have not been tested

@require_POST
def get_profile_picture(request, userid):
    try:
        user = models.User.objects.get(id=userid)
        image_url= Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)

    response_data = {
        'image_url': image_url.image.url if image_url.image else None,
    }

    return JsonResponse(response_data)


# def whoami_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({'isAuthenticated': False})

#     return JsonResponse({'username': request.user.username})
