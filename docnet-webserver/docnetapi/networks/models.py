from django.db import models

# Can be useful in future:
# NETWORK_TYPES = [('LAN', 'Local area network'), ('MAN', 'Metropolitan area network'), ('WAN', 'Wide area network')]


class Network(models.Model):

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)
    cidr = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey('auth.User', related_name='networks', on_delete=models.CASCADE)

    # Can be useful in future:
    # type = models.CharField(choices=NETWORK_TYPES, default='', max_length=100)

    def __str__(self):
        return self.title


class Address(models.Model):

    ip = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='addresses', on_delete=models.CASCADE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
