from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class User(AbstractUser):
#     email = models.EmailField(
#         'email address', 
#         unique=True, 
#     )
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS=['username']
#     cliente = models.BooleanField(
#         'client status',
#         default=True,
#     )

#     def __str__(self):
#         return '{}'.format(self.email)
