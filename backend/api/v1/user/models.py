from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

from v1.character.models import CharacterModel

from utils.generate_api_id import user_id


class GuildRoles(models.TextChoices):
    GUILD_LEADER = ("GUILD_LEADER", "Leader")
    GUILD_OFFICER = ("GUILD_OFFICER", "Officer")
    GUILD_REID_LEADER = ("GUILD_REID_LEADER", "Raid Leader")
    GUILD_RAIDER = ("GUILD_RAIDER", "Raider")
    GUILD_MEMBER = ("GUILD_MEMBER", "Member")


class CustomUserModel(AbstractUser):
    api_user_id: models.CharField = models.CharField(
        default=user_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    username = models.CharField(gettext_lazy("username"), max_length=100, unique=True)
    email = models.EmailField(gettext_lazy("email address"), unique=True)
    guild_role: models.CharField = models.CharField(
        choices=GuildRoles.choices, max_length=100
    )
    characters: models.ManyToManyField = models.ManyToManyField(
        CharacterModel, related_name="custom_user_characters"
    )
    client_id: models.CharField = models.CharField(
        default="", max_length=100, unique=True
    )
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def update_character(self):
        client = self.get_token()

    def __str__(self):
        return self.username
