from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.db import IntegrityError

class UserSerializer(serializers.ModelSerializer):
    
    """
    Serializer for serializing user objects based on the default User model.
    """
    def create(self, validated_data):
        """Method override called to create a new user object in the database

        Args:
            validated_data: Validated data from the .save() method call

        Returns:
            User: The new User object that was just created
        """
        try:
            user = User.objects.create_user(
                username=validated_data['email'],
                email=validated_data['email'],
                password=validated_data['password'],
            )
            return user
        except IntegrityError as e:
            raise serializers.ValidationError(str(e))
        
    class Meta:
        """
        Metadata inner class to support the serializer
        """
        model = User
        fields = ("email", "password")

class LoginSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        # Take username and password from request.data
        username = data.get('email')
        password = data.get('password')

        if username and password:
            # Link: https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView
            # Basically, either use LoginView or authenticate()
            # authenticate() is a low-level method used for custom login/ authentication
            user = authenticate(username= username, password= password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data
    
    class Meta:
        model = User
        fields = ("email", "password" )