# Generated by Django 3.0.8 on 2020-08-18 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('state', models.TextField(default='0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', max_length=550)),
                ('log', models.TextField(default=' ', max_length=1500)),
                ('group', models.CharField(default=' ', max_length=1)),
                ('keywords', models.TextField(default=' ', max_length=300)),
                ('prices', models.TextField(default=' ', max_length=2500)),
                ('budget', models.CharField(default=800, max_length=8)),
                ('academic_position', models.CharField(default=' ', max_length=200)),
            ],
        ),
    ]
