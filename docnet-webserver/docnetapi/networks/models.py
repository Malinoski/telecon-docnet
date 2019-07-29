from django.db import models
NETWORK_TYPES = [('LAN', 'Local area network'), ('MAN', 'Metropolitan area network'), ('WAN', 'Wide area network')]


class Network(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)
    type = models.CharField(choices=NETWORK_TYPES, default='python', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='networks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Address(models.Model):
    ip = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    network = models.ForeignKey(Network, related_name='addresses', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
