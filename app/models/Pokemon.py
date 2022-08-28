from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Pokemon(models.Model):
    name = models.CharField(null=False, max_length=60) #name from pokeapi
    description = models.CharField(max_length=256)

    number = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(1154)], null=False) #id from pokeapi
    types = models.JSONField(null=False) #types from pokeapi
    stats = models.JSONField(null=False) #stats from pokeapi