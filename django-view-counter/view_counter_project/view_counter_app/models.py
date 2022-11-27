from django.db import models

class AppUser(models.Model):
    user_id = models.CharField(max_length=20, unique=True)


