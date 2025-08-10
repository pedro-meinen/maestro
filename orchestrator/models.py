from django.db import models


class Script(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class ExecutionLog(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, related_name="executions")
    executed_at = models.DateTimeField(auto_now_add=True)
    return_code = models.IntegerField(null=True, blank=True)
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)
    success = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.script.name} @ {self.executed_at}"
