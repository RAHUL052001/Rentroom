from django.urls import include, path
from .views import UserViewSet ,RoomListingViewSet ,ContactListViewSet  ,AuthUserViewSet ,S3ImageUploadView # Import your view function
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roomlistings', RoomListingViewSet, basename='roomlisting')
router.register(r'contactlists', ContactListViewSet, basename='contactlist')
router.register(r'authusers', AuthUserViewSet, basename='authuser')  # Register the AuthUser viewset

urlpatterns = [
    path('', include(router.urls)),
    path("upload-to-s3/", S3ImageUploadView.as_view(), name="upload-to-s3"),  # ✅ new S3 uploader
]
