from django.db import models

from v1.classes.models import ClassModel
from v1.spec.models import SpecModel
from v1.serverlist.models import ServerListModel
from utils.generate_api_id import character_id

class FractionEnum(models.TextChoices):
    ALLIANCE = ("Allianz", "alliance")
    HORDE = ("Horde", "horde")


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
    selected_class: models.ForeignKey = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='characters', null=True, blank=True, default=None)
    selected_spec: models.ForeignKey = models.ForeignKey(SpecModel, on_delete=models.CASCADE, related_name='characters', null=True, blank=True, default=None)
    level: models.IntegerField = models.IntegerField()
    faction: models.CharField = models.CharField(choices=FractionEnum.choices, max_length=100, default=FractionEnum.ALLIANCE)
    is_main: models.BooleanField = models.BooleanField(default=False)
    is_internal: models.BooleanField = models.BooleanField(default=False)

    def __str__(self):
        class_name = self.selected_class.name if self.selected_class else None
        spec_info = f"{self.selected_spec.name} ({self.selected_spec.role_type})" if self.selected_spec else None
        main = "Main" if self.is_main else "Alt"
        return f"({main}) {self.name} - {self.realm} - {class_name} - {spec_info} - {self.level} - {self.faction}"
