from django.db import models

NETWORK_TYPES = [('LAN', 'Local area network'), ('MAN', 'Metropolitan area network'), ('WAN', 'Wide area network')]


class Network(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    enabled = models.BooleanField(default=True)
    type = models.CharField(choices=NETWORK_TYPES, default='python', max_length=100)

    class Meta:
        ordering = ['created']
