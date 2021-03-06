# Generated by Django 2.2.3 on 2019-08-01 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('enabled', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='networks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='networks.Network')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
