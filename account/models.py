from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, user, email, profile, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            user=user,
            email=self.normalize_email(email),
            profile=profile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user, email, profile, password):
        user = self.create_user(
            user,
            email,
            profile,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user = models.CharField(verbose_name='user', max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    profile = models.ImageField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['email', 'profile']

    def __str__(self):
        return self.user

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin