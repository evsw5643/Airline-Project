from ast import arg
from locale import normalize
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class Airplane(models.Model):
    def __str__(self):
        return self.airplane_name

    airplane_name = models.CharField(max_length=200)
    airplane_number = models.IntegerField()
    airplane_date_of_departure = models.DateTimeField("Departure date")


# custom User model referenced by https://www.youtube.com/watch?v=HshbjK1vDtY
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        print(user.admin)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser):
    # users will be identified by their email, this ensures no two users share an email
    email = models.EmailField(max_length=255, unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # user can log in
    staff = models.BooleanField(default=False)  # new users are not staff...
    admin = models.BooleanField(default=False)  # or admin
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    def has_perm(self, perm, object=None):
        return True #come back later

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Singleton(models.Model):
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Setting(Singleton):
    backgrounds = (
        ('poop.jpg', 'poop.jpg'),
        ('fuck.jpg', 'fuck.jpg'),
        ('bitch.png', 'bitch.png')
    )
    background_title = models.CharField(max_length=100, choices=backgrounds)
