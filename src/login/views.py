from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import authentication
from django.contrib.auth import login, logout
# from django.shortcuts import render, redirectx


class LoginView(APIView):

    # Link: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    # generates a unique token associated the user if log in successfully
    # TODO: need to test this with a curl or POSTMAN (like I want to see if it does generate a unique token) 
    authentication_classes = [authentication.TokenAuthentication]
    
    # This view should be accessible also for unauthenticated users.
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        #calls upon authenticate method in LoginSerializer
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            #if user is authenticated, it will return a User object
            user = serializer.validated_data['user']
            #login will use this user object to create a session for that user
            #this session is associated with a session cookie stored on the user's browser, which is used to identify the user in subsequent requests.
            #also update user's fields like last_login, IP address, etc
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # a pair with login method
        logout(request)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    
class SignupView(APIView):
    """
    View for the sign-up page's API endpoint.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """POST method for the sign-up page to "call" when a user attempts to create an account
        
        Checks if the request is valid, then creates a new user in the database.

        Args:
            request: The request details.

        Returns:
            Response: The response to return to the user.
        """
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
