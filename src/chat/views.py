import json 
import base64
from django.core.files.base import ContentFile
from django.shortcuts import render
from .serializers import ProfileSerializer, IDESerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Profile
from .models import ChatRoom, IDE
from rest_framework.response import Response
from rest_framework import status


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

@api_view(['GET','PUT', 'POST'])
def ide_view(request, chatroom_id):

    ide = IDE.objects.get(pk=chatroom_id)

    if ide:
        if request.method == 'GET':
            serializer = IDESerializer(ide)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = IDESerializer(ide, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'POST':
            serializer - IDESerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def profile_view(request):

    user_profile = Profile.objects.get(pk=request.data['userid'])

    if user_profile:
        print(user_profile.display_name)

    format, imgstr = request.data['image'].split(';base64,')
    ext = format.split('/')[-1] 
    data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
    
    user_profile.picture = data
    user_profile.save()

    return Response(status=status.HTTP_200_OK)