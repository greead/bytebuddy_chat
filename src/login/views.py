import json

from django.contrib.auth import authenticate, login, logout, models
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST,require_http_methods
from django.db import IntegrityError
from chat.models import Profile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from chat.serializers import ProfileSerializer

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
def get_profile_picture(request):
    try:
        data = json.loads(request.body)
        userid= data.get('userid')
        user = models.User.objects.get(id=userid)
        image_url= Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)
    response_data = {
        'image_url': image_url.picture.url if image_url.picture.url else None,
    }
    return JsonResponse(response_data)

@require_http_methods(["GET", "POST"])
def get_profile(request):
    if request.method == 'GET':
        userid = request.GET.get('userid')
        print(userid)
        if not userid:
            return JsonResponse({'error': 'userid parameter is required for GET requests'}, status=400)

        user = models.User.objects.get(id=userid)
        try:
            profile= Profile.objects.get(user=user) 
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'Image not found'}, status=404)
        url = {
            'image_url': profile.picture.url if profile.picture.url else None,
        }
        return JsonResponse(url)
    
    elif request.method == 'POST':
        # data = json.loads(request.body)
        user = models.User.objects.get(id=1)
        print(request.POST)
        serializer = ProfileSerializer(user, data=request.POST.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        userid= request.POST.get('userid', '')
        print(userid)
        name = request.POST.get('name', '')
        print(name)
        bio = request.POST.get('bio','')
        print(bio)
        pic = request.FILES.get('img')
        try:
            user = models.User.objects.get(id=userid)
            profile= Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'Image not found'}, status=404)
        if (name is not None):
            profile.display_name = name

        if (bio is not None):
            profile.bio = bio

        if(pic is not None):
            profile.picture = pic
        return JsonResponse({'detail': 'Successfully updated profile.'})
    
# def whoami_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({'isAuthenticated': False})

#     return JsonResponse({'username': request.user.username})
