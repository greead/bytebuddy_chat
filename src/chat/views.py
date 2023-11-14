from django.shortcuts import render
from .serializers import ProfileSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Profile
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

#function to get all users and add new user
@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        users = Profile.objects.all()
        if users is not None:
            serializer = ProfileSerializer(users, many=True)
            return JsonResponse({"users":serializer.data})
        return JsonResponse("no data found")
    
    if request.method =='POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("invalid request")
  

#perfom actions on user based on ID
@api_view(['GET', 'PUT', 'DELETE'])      
def UserprofilewithID(request,id):
    try:
        user = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def startapp(request):
    return render(request, 'index.html')
