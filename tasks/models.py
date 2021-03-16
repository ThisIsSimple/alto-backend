from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    priorityOptions = (
        (1, _('none')),
        (2, _('low')),
        (3, _('normal')),
        (4, _('high')),
        (5, _('urgent')),
    )

    task_name = models.CharField(_("task_name"), max_length=255, default='')
    priority = models.IntegerField(
        _("priority"), choices=priorityOptions, default=1)
    description = models.TextField(_("description"), blank=True, null=True)
    owner = models.ForeignKey("users.CustomUser", verbose_name=_(
        "owner"), on_delete=models.CASCADE)
    start_date = models.DateField(_("start_date"), blank=True, null=True)
    end_date = models.DateField(_("end_date"), blank=True, null=True)
    secret = models.BooleanField(_("secret"), blank=True, null=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.task_name, self.owner.name)


class TaskProgress(models.Model):
    statusOptions = (
        ('unread', _('unread',)),
        ('working', _('working',)),
        ('reported', _('reported',)),
        ('pending', _('pending',)),
        ('rejected', _('rejected',)),
        ('completed', _('completed',)),
        ('canceled', _('canceled',))
    )

    task = models.ForeignKey("tasks.Task", verbose_name=_(
        "task_id"), on_delete=models.CASCADE, related_name="progresses")
    ordered_by = models.ForeignKey("users.CustomUser", verbose_name=_(
        "ordered_by"), on_delete=models.CASCADE, related_name="ordered_by_user_id")
    ordered_to = models.ForeignKey("users.CustomUser", verbose_name=_(
        "ordered_to"), on_delete=models.CASCADE, related_name="ordered_to_user_id")
    status = models.CharField(
        _("status"), choices=statusOptions, max_length=15, default='unread')
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return "{} : {} -> {}".format(self.task.name, self.ordered_by.name, self.ordered_to.name)


# class TaskChecklist ...
