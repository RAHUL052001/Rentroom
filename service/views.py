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
        
     


from rest_framework import viewsets, permissions
from .models import RoomListing
from .serializers import RoomListingSerializer

from rest_framework import serializers

class RoomListingViewSet(viewsets.ModelViewSet):
    queryset = RoomListing.objects.all().order_by("-created_at")
    serializer_class = RoomListingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user_id = self.request.data.get("room_owner")  # coming from frontend

        if not user_id:
            raise serializers.ValidationError({"room_owner": "This field is required."})

        try:
            user_instance = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"room_owner": "Invalid user ID."})

        serializer.save(room_owner=user_instance)


class ContactListViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing ContactList instances.
    """
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated to access this viewset

# service/views.py
import boto3, uuid
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import datetime

class S3ImageUploadView(APIView):
    permission_classes = [permissions.AllowAny]  # change if you need auth

    def post(self, request):
        file_obj = request.FILES.get("file")  # frontend must send as form-data "file"
        if not file_obj:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate unique filename with date
        now = datetime.now().strftime("%Y-%m-%d")
        file_extension = file_obj.name.split(".")[-1]
        file_name = f"uploads/{now}/{uuid.uuid4()}.{file_extension}"

        # Upload to S3
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )

        s3.upload_fileobj(file_obj, settings.AWS_STORAGE_BUCKET_NAME, file_name)

        # Public URL
        file_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{file_name}"

        return Response(
            {
                "message": "Image uploaded successfully",
                "url": file_url,
                "path": file_name,
            },
            status=status.HTTP_201_CREATED,
        )


