"""
serializers.py
This module contains serializers for the User, RoomListing, and ContactList models.

"""

from rest_framework import serializers

from .models import User, RoomListing , ContactList ,AuthUser


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ["id", "email", "password", "is_active", "is_staff"]  
        extra_kwargs = {
            "password": {"write_only": True}  # don't return password in API response
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = AuthUser(**validated_data)
        print(password)
        if password:
            user.set_password(password)  # hash password
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # hash on update
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.This serializer includes all fields from the User model.
    """
    class Meta:
        """
        Meta class for UserSerializer.
        """
        model = User
        fields = '__all__'

class RoomListingSerializer(serializers.ModelSerializer):
    """
    RoomListingSerializer is a serializer for the RoomListing model.
    """
    class Meta:
        """ Meta class for RoomListingSerializer."""
        model = RoomListing
        fields = '__all__'

class ContactListSerializer(serializers.ModelSerializer):
    """
    ContactListSerializer is a serializer for the ContactList model."""
    class Meta:
        """ Meta class for ContactListSerializer."""
        model = ContactList
        fields = '__all__'





