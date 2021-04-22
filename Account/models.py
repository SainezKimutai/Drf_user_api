from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
from .managers import UserManager
# from django.utils.translation import ugettext_lazy as _


def get_profile_image_filepath(self):
    return f"images/{self.pk}/{'profile_image.png'}"


def get_default_profile_image():
    return "user.png"


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined",
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,
                                      upload_to=get_profile_image_filepath,
                                      null=True,
                                      blank=True,
                                      default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = UserManager()

    # Allow user to login with email rather than username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

    def get_profile_image_filename(self):
        return str(self.profile_image[str(self.profile_image).index(f'images/{self.pk}/'):])
