from django.db import models


class Robot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    powermove = models.TextField()
    experience = models.IntegerField()
    outOfOrder = models.BooleanField()
    avatar = models.URLField()
