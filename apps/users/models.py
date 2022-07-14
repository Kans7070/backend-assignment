from django.db import models
from apps.users.manager import UserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=50, unique=True, null=False, blank=False)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=False, blank=False)
    zip = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def _str_(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, add_labels):
        return True,
