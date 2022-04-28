from ast import arg
from locale import normalize
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class Airplane(models.Model):
    def __str__(self):
        return self.airplane_name
    airplane_name = models.CharField(max_length=200)
    airplane_number = models.IntegerField()
    airplane_destination = models.CharField(max_length=255, blank=True)
    airplane_date_of_departure = models.DateTimeField(
        null=True, verbose_name="Departure date")


# custom User model referenced by https://www.youtube.com/watch?v=HshbjK1vDtY
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, date_of_birth, password=None):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        if not full_name:
            raise ValueError("Full name is required")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        print(user.admin)
        user.save(using=self._db)
        return user

    def create_staffuser(self, full_name, email, date_of_birth, password):
        user = self.create_user(
            email,
            full_name=full_name,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, date_of_birth, password):
        user = self.create_user(
            email,
            full_name=full_name,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):  # might add a DoB
    # users will be identified by their email, this ensures no two users share an email
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    full_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    active = models.BooleanField(default=True)  # user can log in
    staff = models.BooleanField(default=False)  # new users are not staff...
    admin = models.BooleanField(default=False)  # or admin
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, object=None):
        return True  # come back later

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


class Booking(models.Model):

    FOOD_CHOICES = (
        ('Blackened Chicken', 'Blackened Chicken'),
        ('New York Strip', 'New York Strip'),
        ('Escargot', 'Escargot'),
        ('Caviar', 'Caviar'),
        ('Oysters', 'Oysters'),
        ('Foie Gras', 'Foie Gras'),
        ('Rocky Mountain Oysters', 'Rocky Mountain Oysters'),
        ('Creme Brulee', 'Creme Brulee'),
        ('Wagu Beef', 'Wagu Beef'),
        ('Baby Back Ribs', 'Baby Back Ribs'),
        ('Chicken Parmesean', 'Chicken Parmesean'),
        ('Nigiri', 'Nigiri')
    )
    DRINK_CHOICES = (
        ('Aperol Spritz', 'Aperol Spritz'),
        ('Jack and Coke', 'Jack and Coke'),
        ('Rum and Coke', 'Rum and Coke'),
        ('White Wine', 'White Wine'),
        ('Red Wine', 'Red Wine'),
        ('Champagne', 'Champagne'),
        ('Aperol Spritz', 'Aperol Spritz'),
        ('Screwdriver', 'Screwdriver'),
        ('Bloody Mary', 'Bloody Mary'),
        ('Pilsner', 'Pilsner'),
        ('IPA', 'IPA')
    )
    MOVIE_CHOICES = (
        ('Batman', 'Batman'),
        ('Moonfall', 'Moonfall'),
        ('Interstellar', 'Interstellar'),
        ('Soul Plane', 'Soul Plane'),
        ('The Adam Project', 'The Adam Project'),
        ('Spiderman', 'Spiderman'),
        ('X', 'X'),
        ('Screwdriver', 'Screwdriver'),
        ('Choose or Die', 'Choose or Die'),
        ('Power Rangers', 'Power Rangers'),
        ('Knives Out', 'Knives Out'),
        ('Power Rangers', 'Power Rangers'),
        ('Suck on That!', 'Suck on That!'),
        ('My Friend Clifford', 'My Friend Clifford'),
        ('Dick Wildfreds Unlikely Adventure', 'Dick Wildfreds Unlikely Adventure'),
        ('Dwight Schrute', 'Dwight Schrute')
    )
    airplane = models.ForeignKey(
        Airplane,
        verbose_name="Airplane",
        on_delete=models.CASCADE,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    food_selection = models.CharField(
        max_length=255,
        choices=FOOD_CHOICES,
        default='BR',
    )
    drink_selection = models.CharField(
        max_length=255,
        choices=DRINK_CHOICES,
        blank=True)
    movie_selection = models.CharField(
        max_length=255,
        choices=MOVIE_CHOICES,
        blank=True)

    cost = models.DecimalField(
        name="cost", decimal_places=2, max_digits=6, null=True)

    def __str__(self):
        return '%s%s%s%s%s' % ("booking", "_", self.user, "_", self.airplane)


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
