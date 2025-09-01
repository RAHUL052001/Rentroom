from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomListing, ContactList, User,AuthUser
from .serializers import UserSerializer, ContactListSerializer , AuthUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




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
    
    @action(detail=False, methods=["get"], url_path=r"check-user/(?P<user_id>\d+)")
    def check_user(self, request, user_id=None):
        """
        Check if a user exists by ID.
        URL: /api/users/check-user/<user_id>/
        """
        try:
            user = AuthUser.objects.get(pk=user_id)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="check-user")
    def check_user(self, request):
        email = request.query_params.get("email")
        if not email:
            return Response({"error": "email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
     


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

