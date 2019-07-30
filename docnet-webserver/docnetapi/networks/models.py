from django.db import models
# NETWORK_TYPES = [('LAN', 'Local area network'), ('MAN', 'Metropolitan area network'), ('WAN', 'Wide area network')]


class Network(models.Model):

    # Classless Inter-Domain Routing. Ex.: "192.168.0.0 /24", "192.168.0.0 /22", "2002:C0A8::/48"
    cidr = models.CharField(max_length=100, blank=False)

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)
    # type = models.CharField(choices=NETWORK_TYPES, default='', max_length=100)

    # Relationship one to one (fk and pk)
    owner = models.ForeignKey('auth.User', related_name='networks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Address(models.Model):

    # Attributes
    ip = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User', related_name='addresses', on_delete=models.CASCADE)

    # Relationship one to one (one address has only one network)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
