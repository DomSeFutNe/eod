from rest_framework import serializers

from .models import ServerListModel


class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerListModel
        fields = ["api_server_list_id", "name", "region"]