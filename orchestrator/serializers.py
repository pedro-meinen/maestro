from rest_framework import serializers

from orchestrator.models import ExecutionLog, Script


class ScriptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = "__all__"


class ExecutionLogSerializer(serializers.ModelSerializer):
    script_name = serializers.CharField(source="script.name", read_only=True)

    class Meta:
        model = ExecutionLog
        fields = [
            "id",
            "script",
            "script_name",
            "executed_at",
            "return_code",
            "stdout",
            "stderr",
            "success",
        ]
