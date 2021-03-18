from django.db import models
from django.utils.translation import ugettext_lazy as _


class Report(models.Model):
    task_progress = models.OneToOneField("tasks.TaskProgress", verbose_name=_(
        "task_progress_id"), on_delete=models.CASCADE, related_name="report")
    report_name = models.CharField(
        _("report_name"), max_length=255, default='')
    report_content = models.TextField(
        _("report_content"), blank=True, null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
