from django.db import models


class Network(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
