from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, EmailField
from django.forms.forms import Form

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return {self.first_name}

    def __str__(self):
        return {self.last_name}
# Create your models here.
