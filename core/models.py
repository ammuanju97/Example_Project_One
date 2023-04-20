from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserRegister(models.Model):
    fullname = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    password = models.CharField(max_length=8, null=False, blank=False)
    address1 = models.CharField(max_length=120, null=False, blank=False)
    address2 = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    pin_code = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return self.fullname


class SignUpModel(AbstractUser):
    fullname = models.CharField(max_length=30, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=256, null=False, blank=False)
    address1 = models.CharField(max_length=120, null=False, blank=False)
    address2 = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    state = models.CharField(max_length=255, null=False, blank=False)
    pin_code = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "SignUpModel"
