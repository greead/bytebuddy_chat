import json
from django.http import JsonResponse, HttpRequest, HttpResponse
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout, authenticate
from django.middleware.csrf import get_token

# Get CSRF token
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

class LoginView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        username = data['email']
        password = data['password']

        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is None:
            return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

        login(request, user)
        response = Response({'detail': 'Successfully logged in.'})
        return response

class LogoutView(APIView):
    def post(self, request: HttpRequest):
        print(request.user)
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})
    
class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if request.data.get('password') != request.data.get('confirmPw'):
            return Response({'error':'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
