from django.db import models

# Create your models here9.
class BaseMeter(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)