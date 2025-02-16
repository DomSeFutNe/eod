from rest_framework import serializers

from v1.spec.serializers import SpecSerializer
from .models import ClassModel


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'
        
class SelectedClassSerializer(serializers.ModelSerializer):
    available_specs = SpecSerializer(many=True, read_only=True)
    class Meta:
        model = ClassModel
        fields = ["api_class_id", "name", "available_specs"]