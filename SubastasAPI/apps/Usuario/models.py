from django.db import models
from django.contrib.auth.models import AbstractUser



class Usuario(models.Model):
    pass
    # """ Extra fields"""
    # email = models.EmailField(
    #     'email address', 
    #     unique=True, 
    # )
    # # USERNAME_FIELD = 'username'
    # # REQUIRED_FIELDS=['username']
    # # cliente = models.BooleanField(
    # #     'client status',
    # #     default=True,
    # # )

    # def __str__(self):
    #     return '{}'.format(self.username)
