from django.db import models

from v1.spec.models import SpecModel
from utils.generate_api_id import class_id

# Create your models here.
class ClassModel(models.Model):
    api_class_id: models.CharField = models.CharField(
        default=class_id,
        unique=True,
        primary_key=True,
        editable=False,
        max_length=255,
    )
    name: models.CharField = models.CharField(max_length=100)
    class_id: models.IntegerField = models.IntegerField()
    available_specs: models.ManyToManyField = models.ManyToManyField(SpecModel, related_name='classes')

    def __str__(self):
        specs = self.available_specs.all()
        spec_names = ', '.join([f"({spec.role_type}) {spec.name}" for spec in specs])
        return f"{self.name} - {specs.__len__()} Specs: {spec_names}"