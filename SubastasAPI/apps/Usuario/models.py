from django.db import models
from django.contrib.auth.models import AbstractUser



class Usuario(models.Model):
    pass
    # email = models.EmailField(
    #     'email address',
    #     unique=True,
    # )

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    # is_client = models.BooleanField(
    #     'client',
    #     default=True,
    # )

    # def __str__(self):
    #     return self.username

