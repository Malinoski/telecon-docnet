from django.db import models
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

NETWORK_TYPES = [('LAN', 'Local area network'), ('MAN', 'Metropolitan area network'), ('WAN', 'Wide area network')]


class Network(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    enabled = models.BooleanField(default=True)
    type = models.CharField(choices=NETWORK_TYPES, default='python', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='networks', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']
