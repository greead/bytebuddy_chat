from django.shortcuts import render
import requests 
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.mixins import LoginRequireMixin, User
from rest_framework import permissions

# class LoginView(LoginRequireMixin, TemplateView):
#     template_name = "login.html"

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
