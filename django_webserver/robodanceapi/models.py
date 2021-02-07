from django.db import models


class Robot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    powermove = models.TextField()
    experience = models.IntegerField()
    outOfOrder = models.BooleanField()
    avatar = models.URLField()


class DanceOff(models.Model):
    id = models.AutoField(primary_key=True)
    winner = models.ForeignKey(
        Robot, on_delete=models.CASCADE, related_name='wins')
    loser = models.ForeignKey(
        Robot, on_delete=models.CASCADE, related_name='loses')
    dancedAt = models.DateTimeField(auto_now_add=True)
