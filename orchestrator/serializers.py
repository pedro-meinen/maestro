from rest_framework import serializers

from orchestrator.models import Script


class ScriptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = "__all__"
