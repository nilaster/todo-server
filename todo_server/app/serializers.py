from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = (
            "id",
            "title",
            "priority",
            "due_on",
            "status",
            "created_on",
        )
        read_only_fields = (
            "id",
            "created_on",
        )
