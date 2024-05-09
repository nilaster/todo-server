from rest_framework.viewsets import ModelViewSet
from . import models, serializers


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
