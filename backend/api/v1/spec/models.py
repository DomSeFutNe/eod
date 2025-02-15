from django.db import models
from utils.generate_api_id import spec_id

# Create your models here.
class SpecModel(models.Model):
    api_spec_id: models.CharField = models.CharField(
        default=spec_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    name: models.CharField = models.CharField(max_length=255)
    role_type: models.CharField = models.CharField(max_length=255)
    class_id: models.IntegerField = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.class_id}) {self.name} - {self.role_type}"