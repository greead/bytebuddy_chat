from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# TODO
# class LoginView(LoginRequireMixin, TemplateView):
#     template_name = "login.html"

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
