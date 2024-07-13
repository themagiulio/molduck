import uuid

from django.db import models
from django.conf import settings


class Job(models.Model):
    uuid = models.UUIDField(
        verbose_name="UUID",
        editable=False,
        default=uuid.uuid4,
    )
    """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    """
    success = models.BooleanField(default=False)
    input_data = models.JSONField()
    output_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.uuid)
