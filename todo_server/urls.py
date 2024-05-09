from rest_framework.routers import SimpleRouter
from todo_server.app.views import TaskViewSet


router = SimpleRouter()
router.register("tasks", TaskViewSet)


urlpatterns = router.urls
