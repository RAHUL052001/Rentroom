"""
serializers.py
This module contains serializers for the User, RoomListing, and ContactList models.

"""

from rest_framework import serializers

from .models import User, RoomListing , ContactList


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