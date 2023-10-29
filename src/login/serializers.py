from django.contrib.auth.models import User
from rest_framework import serializers

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
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    
    class Meta:
        """
        Metadata inner class to support the serializer
        """
        model = User
        fields = ("email", "password" )