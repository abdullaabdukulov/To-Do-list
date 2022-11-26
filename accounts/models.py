from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    User Info
    """
    #The user registers with a email, so the name, birthday and email address can be empty
    name = models.CharField("Name",max_length=30, null=True, blank=True)
    # password = 
    email = models.EmailField("Mail",max_length=100, null=True, blank=True)

    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return self.username