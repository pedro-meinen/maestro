from django.db import models


class Script(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
