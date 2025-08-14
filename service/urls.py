from django.urls import include, path
from .views import UserViewSet ,RoomListingViewSet ,ContactListViewSet  ,AuthUserViewSet # Import your view function
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roomlistings', RoomListingViewSet, basename='roomlisting')
router.register(r'contactlists', ContactListViewSet, basename='contactlist')
router.register(r'authusers', AuthUserViewSet, basename='authuser')  # Register the AuthUser viewset

urlpatterns = [
    # Define your URL patterns here
    path('', include(router.urls))
]