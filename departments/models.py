from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    name = models.TextField(_("name"), max_length=30)
    description = models.TextField(_("description"), blank=True, null=True)
    department_image = models.ImageField(
        _("department image"), upload_to="departments", blank=True, null=True)
    director = models.ForeignKey("users.CustomUser", blank=True,
                                 null=True, on_delete=models.SET_NULL, related_name="director_id")
    founded_at = models.DateTimeField(_("founded_at"), blank=True, null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.name
