from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orchestrator.views import ExecutionLogListView, ScriptViewSet

router = DefaultRouter()
router.register(r"scripts", ScriptViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("executions/", ExecutionLogListView.as_view(), name="execution-log"),
]
