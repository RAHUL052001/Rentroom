from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomListing, ContactList, User,AuthUser
from .serializers import UserSerializer, ContactListSerializer , AuthUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action



# Create your views here.




class AuthUserViewSet(viewsets.ModelViewSet):
    print("ooooooooooooooooo")
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return response({"error": "Email and password required"}, status=400)

        # ✅ This ensures password hashing happens
        print("222222222222222222222222")
        user = AuthUser.AuthUserManager.create_user(email=email, password=password)

        return response({"message": "User created", "email": user.email}, status=201)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    

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

