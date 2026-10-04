from django.urls import include, path

# from service.views import INP_CASEViewSet ,INP_CASE_METAViewSet ,INP_MILESTONEViewSet
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'cases', INP_CASEViewSet, basename='case')
router.register(r'case-meta', INP_CASE_METAViewSet, basename='case-meta')
router.register(r'milestones', INP_MILESTONEViewSet, basename='milestone')

urlpatterns = [
    path('', include(router.urls)),
]
