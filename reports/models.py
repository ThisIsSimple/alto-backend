from django.db import models
from django.utils.translation import ugettext_lazy as _


class Report(models.Model):
    task = models.ForeignKey("tasks.Task", verbose_name=_(
        "task_id"), on_delete=models.CASCADE)
    report_name = models.CharField(_("task_name"), max_length=255, default='')
    report_content = models.TextField(_("description"), blank=True, null=True)
    report_writer = models.ForeignKey("users.CustomUser", verbose_name=_(
        "owner"), on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
