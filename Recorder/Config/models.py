from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Config(models.Model):
    key = CharField(max_length=255, primary_key=True)
    value = CharField(max_length=255)