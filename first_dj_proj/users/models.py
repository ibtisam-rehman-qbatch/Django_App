from django.db import models
from django.utils import timezone

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joinedDate = models.DateField(default= timezone.now)

# Create your models here.
