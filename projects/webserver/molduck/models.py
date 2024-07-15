import uuid

from django.db import models


class Job(models.Model):
    class Status(models.IntegerChoices):
        AWAITING = 1, "awaiting"
        RUNNING = 2, "running"
        FAILED = 3, "failed"
        SUCCEDED = 4, "succeded"

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
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.AWAITING,
    )
    input_data = models.JSONField()
    output_data = models.JSONField(null=True, blank=True)

    @property
    def success(self) -> bool:
        return self.status == Job.Status.SUCCEDED

    def __str__(self):
        return str(self.uuid)
