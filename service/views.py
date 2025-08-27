from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomListing, ContactList, User,AuthUser
from .serializers import UserSerializer, ContactListSerializer , AuthUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action



# Create your views here.




class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return response({"error": "Email and password required"}, status=400)

        # ✅ This ensures password hashing happen
        user = AuthUser.AuthUserManager.create_user(email=email, password=password)

        return response({"message": "User created", "email": user.email}, status=201)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset

    @action(detail=False, methods=["get"], url_path="check-user/(?P<username>[^/.]+)")
    def check_user(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return response(serializer.data)
        except User.DoesNotExist:
            return response({"error": "User not found"}, status=404)

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

