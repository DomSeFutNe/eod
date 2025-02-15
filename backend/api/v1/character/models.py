from django.db import models

from v1.serverlist.models import ServerListModel
from utils.generate_api_id import character_id


class CharacterModel(models.Model):
    api_character_id: models.CharField = models.CharField(
        default=character_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    name: models.CharField = models.CharField(max_length=100)
    id: models.IntegerField = models.IntegerField()
    realm: models.ForeignKey = models.ForeignKey(
        ServerListModel,
        on_delete=models.CASCADE,
        related_name='characters'
    )
    class_name: models.CharField = models.CharField(max_length=100)
    level: models.IntegerField = models.IntegerField()
    faction: models.CharField = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.realm} - {self.class_name} - {self.level} - {self.faction}"
