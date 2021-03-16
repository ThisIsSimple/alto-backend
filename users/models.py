from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

import datetime


class CustomUser(AbstractUser):
    username = models.CharField(_("username"), max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_("name"), max_length=30)
    nickname = models.CharField(
        _("nickname"), max_length=50, blank=True, null=True)
    profile = models.TextField(_("profile"), blank=True, null=True)
    profile_image = models.ImageField(
        _("profile image"), upload_to="profiles", blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=11,
                             unique=True, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    entered_at = models.DateField(_("entered at"), blank=True, null=True)
    rank = models.ForeignKey('ranks.Rank', verbose_name=_(
        "rank id"), on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(
        _("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return "{} {}".format(self.username, self.name)
