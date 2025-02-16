from rest_framework import serializers

from v1.serverlist.serializers import ServerListSerializer
from v1.spec.serializers import SpecSerializer
from v1.classes.serializer import SelectedClassSerializer

from .models import CharacterModel


class CharacterSerializer(serializers.ModelSerializer):
    selected_class = SelectedClassSerializer(read_only=True)
    selected_spec = SpecSerializer(read_only=True)
    realm = ServerListSerializer(read_only=True)

    class Meta:
        model = CharacterModel
        fields = [
            "api_character_id",
            "name",
            "selected_class",
            "selected_spec",
            "realm",
            "level",
            "faction",
            "is_main",
            "is_internal",
        ]
