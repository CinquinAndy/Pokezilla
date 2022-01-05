from django.db import models


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name_en = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)
