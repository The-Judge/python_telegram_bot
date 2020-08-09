from django.db import models


class User(models.Model):
    user_id     = models.IntegerField(unique=True, primary_key=True)
    first_name  = models.CharField(max_length=64)
    last_name   = models.CharField(max_length=64)
