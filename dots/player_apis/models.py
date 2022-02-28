from django.db import models

# Create your models here.
class player_data(models.Model):
    username = models.CharField(max_length=2048)
    xp = models.IntegerField(blank=True, default=0)
    gold = models.IntegerField(blank=True, default=0)
    