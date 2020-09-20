from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username should be given to create an account")
        if not email:
            raise ValueError("Email should be give to create an account")
        user = self.model(username=username,
                          email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=30, blank=False, null=False, verbose_name="Username")
    email = models.EmailField(
        max_length=255, blank=False, null=False, unique=True, verbose_name="Email")
    gender = models.CharField(
        max_length=10, blank=False, null=False, verbose_name="Gender")

    first_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Last Name")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"


class Product(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"
