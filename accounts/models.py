from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from .utility import generate_random_email

class UserManager(BaseUserManager):

    def create_user(self, username, email,password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email = self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password,
            is_staff=True
        )
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):

    username = models.SlugField(max_length=32, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=128, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] # Email & Password are required by default.

    objects = UserManager()

    def get_fullname(self):
        return self.fullname

    def get_username(self):
        return self.username

    # def get_email(self):
    #     return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
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
