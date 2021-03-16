from django.db import models
from django.utils.translation import ugettext_lazy as _


class Attachment(models.Model):
    attachment_name = models.TextField(_("attachment_name"))
    attachment_type = models.CharField(
        _("attachment_type"), max_length=255, blank=True, null=True)
    attachment_file = models.FileField(
        upload_to="attachments", max_length=255)
    # task, report, etc.
    parent_type = models.CharField(_("parent_type"), max_length=50)
    parent = models.IntegerField(_("parent_id"))
    uploader = models.ForeignKey("users.CustomUser", verbose_name=_(
        "uploader"), on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
