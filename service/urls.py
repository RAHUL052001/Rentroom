from django.urls import include, path
from .views import UserViewSet ,RoomListingViewSet ,ContactListViewSet  # Import your view function
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'roomlistings', RoomListingViewSet, basename='roomlisting')
router.register(r'contactlists', ContactListViewSet, basename='contactlist')

urlpatterns = [
    # Define your URL patterns here
    path('', include(router.urls))
]