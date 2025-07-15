from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomListing, ContactList, User
from .serializers import UserSerializer, ContactListSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset

class RoomListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing RoomListing instances.
    """
    queryset=RoomListing.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this view

class ContactListViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing ContactList instances.
    """
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset