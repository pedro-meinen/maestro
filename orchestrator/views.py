import json

from django.db import models
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from orchestrator.models import ExecutionLog, Script
from orchestrator.serializers import ExecutionLogSerializer, ScriptSerializers
from orchestrator.tasks import run_script


class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializers

    @action(detail=True, methods=["post"])
    def execute(self, _: Request, pk: int | None = None) -> Response:
        task = run_script.delay(pk or 0)
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


class ExecutionLogListView(generics.ListAPIView):
    queryset = ExecutionLog.objects.all().order_by("-executed_at")
    serializer_class = ExecutionLogSerializer

    def get_queryset(self) -> models.QuerySet:
        script_id = self.request.query_params.get("script_id")
        if script_id:
            return self.queryset.filter(script_id=script_id)
        return self.queryset
