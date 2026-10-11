from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


from .models import INP_CASE, INP_CASE_META, INP_MILESTONE
from .serializers import INP_CASESerializer ,INP_CASE_METASerializer ,INP_MILESTONESerializer


class INP_CASEViewSet(viewsets.ModelViewSet):
    serializer_class = INP_CASESerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Only return flagged room listings (is_flagged=True)
        """
        return INP_CASE.objects.all()
    def post(self, request, *args, **kwargs):
        """
        Create a new INP_CASE and its initial milestone.
        """

        with transaction.atomic():

            # 1. Create Case
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            case = serializer.save()


        # Return Case response
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class INP_CASE_METAViewSet(viewsets.ModelViewSet):
    serializer_class = INP_CASE_METASerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Only return flagged room listings (is_flagged=True)
        """
        return INP_CASE_META.objects.all()
    def post(self, request, *args, **kwargs):
        """
        Create a new INP_CASE_META instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class INP_MILESTONEViewSet(viewsets.ModelViewSet):
    serializer_class = INP_MILESTONESerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Only return flagged room listings (is_flagged=True)
        """
        return INP_MILESTONE.objects.all()
    def post(self, request, *args, **kwargs):
        """
        Create a new INP_MILESTONE instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    



