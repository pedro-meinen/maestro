from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orchestrator.views import ScriptViewSet

router = DefaultRouter()
router.register(r"scripts", ScriptViewSet)

urlpatterns = [path("", include(router.urls))]
