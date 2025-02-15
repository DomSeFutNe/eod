from django.db import models

from utils.generate_api_id import server_list_id


class ServerListModel(models.Model):
    api_server_list_id: models.CharField = models.CharField(
        default=server_list_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    name: models.CharField = models.CharField(max_length=100)
    region: models.CharField = models.CharField(
        max_length=100,
        default="EU",
        choices=[("EU", "eu"), ("US", "us"), ("KR", "kr"), ("TW", "tw"), ("CN", "cn")],
    )
    blizzard_id: models.IntegerField = models.IntegerField()
    blizzard_slug: models.CharField = models.CharField(max_length=100)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.region} - {self.name}"
