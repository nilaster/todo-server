from django.urls import path
from rest_framework.routers import SimpleRouter
from todo_server.app.views import TaskViewSet, HealthCheckView


router = SimpleRouter()
router.register("tasks", TaskViewSet)


urlpatterns = [
    path("", HealthCheckView.as_view(), name="health-check"),
] + router.urls
