from rest_framework import serializers

from .models import SpecModel

class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecModel
        fields = ['api_spec_id', 'name', 'role_type']