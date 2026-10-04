

from rest_framework import serializers

from .models import INP_CASE,INP_CASE_META, INP_MILESTONE

class INP_CASESerializer(serializers.ModelSerializer):
    """
    Serializer for the INP_CASE model.This serializer includes all fields from the INP_CASE model.
    """
    class Meta:
        """
        Meta class for INP_CASESerializer.
        """
        model = INP_CASE
        fields = '__all__'


class INP_CASE_METASerializer(serializers.ModelSerializer):
    """
    Serializer for the INP_CASE_META model.This serializer includes all fields from the INP_CASE_META model.
    """
    class Meta:
        """
        Meta class for INP_CASE_METASerializer.
        """
        model = INP_CASE_META
        fields = '__all__'


class INP_MILESTONESerializer(serializers.ModelSerializer):
    """
    Serializer for the INP_MILESTONE model.This serializer includes all fields from the INP_MILESTONE model.
    """
    class Meta:
        """
        Meta class for INP_MILESTONESerializer.
        """
        model = INP_MILESTONE
        fields = '__all__'