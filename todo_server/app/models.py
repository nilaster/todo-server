from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"

    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED"
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"

    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=Priority.choices)
    due_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NOT_STARTED
    )
    created_on = models.DateTimeField(auto_now_add=True)
