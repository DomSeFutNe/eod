from v1.character.serializers import CharacterSerializer
from .models import CustomUserModel
from rest_framework import serializers
from django.contrib.auth.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    characters = CharacterSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomUserModel
        fields = [
            "api_user_id",
            "username",
            "email",
            "is_staff",
            "characters",
            "guild_role",
        ]
        read_only_fields = ["is_staff", "characters"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
