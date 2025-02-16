from django.db import models

from v1.character.models import CharacterModel
from v1.user.models import CustomUserModel
from utils.generate_api_id import discord_acc_id


# Create your models here.
class DiscordAccountModel(models.Model):
    api_discord_acc_id: models.CharField = models.CharField(
        default=discord_acc_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    accId: models.BigIntegerField = models.BigIntegerField(unique=True, default=0)
    name: models.CharField = models.CharField(max_length=255, default="")
    attended: models.BigIntegerField = models.BigIntegerField(default=0)
    percentage: models.FloatField = models.FloatField(default=0.0)
    connected_user: models.ForeignKey = models.ForeignKey(
        CustomUserModel,
        related_name="custom_user",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )
    connected_characters: models.ManyToManyField = models.ManyToManyField(
        CharacterModel,
        related_name="characters",
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.percentage}%"
