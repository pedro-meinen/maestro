import json

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from orchestrator.models import Script
from orchestrator.serializers import ScriptSerializers
from orchestrator.tasks import run_script


class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializers

    @action(detail=True, methods=["post"])
    def execute(self, _: Request, pk: int | None = None) -> Response:
        task = run_script.delay(pk)
        return Response({"task_id": task.id})

    @action(detail=True, methods=["post"])
    def schedule(self, request: Request, pk: int | None = None) -> Response:
        cron = request.data.get("cron", {})
        schedule, _ = CrontabSchedule.objects.get_or_create(**cron)
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f"Run script {pk}",
            task="orchestrator.tasks.run_script",
            args=json.dumps([pk]),
        )
        return Response({"status": "scheduled"})
