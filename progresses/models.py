from django.db import models
from django.utils.translation import ugettext_lazy as _


class Progress(models.Model):
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
