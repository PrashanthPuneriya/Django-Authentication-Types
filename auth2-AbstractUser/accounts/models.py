from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In Django USERNAME_FIELD is a unique identifier i.e. nickname of the user but not technically username
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
