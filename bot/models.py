from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id     = models.IntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Message(models.Model):
    update_id       = models.IntegerField(unique=True)
    text            = models.TextField(max_length=4096)
    date            = models.DateTimeField(default=timezone.now)
    sender          = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'
