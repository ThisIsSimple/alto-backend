from django.db import models
from django.utils.translation import ugettext_lazy as _


class Rank(models.Model):
    name = models.TextField(_("name"), max_length=30)
    rank_image = models.ImageField(
        _("rank image"), upload_to="ranks", blank=True, null=True)
    level = models.IntegerField(_("level"), default=0)

    def __str__(self):
        return self.name
