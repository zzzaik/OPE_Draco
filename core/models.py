from django.db import models

# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=95)
    senha = models.CharField(max_length=300)