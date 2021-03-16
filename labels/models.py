from django.db import models
from django.utils.translation import ugettext_lazy as _


class Label(models.Model):
    name = models.CharField(_("name"), max_length=30)
    color = models.CharField(
        _("color"), max_length=7, default="#000000", null=True, blank=True)


class LabelTask(models.Model):
    label = models.ForeignKey("labels.Label", verbose_name=_(
        "label_id"), on_delete=models.CASCADE)
    task = models.ForeignKey("tasks.Task", verbose_name=_(
        "task_id"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
