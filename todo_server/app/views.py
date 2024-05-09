from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response(status=200)
