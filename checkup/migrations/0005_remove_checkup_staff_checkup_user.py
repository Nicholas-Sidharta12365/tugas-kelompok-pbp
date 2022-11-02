# Generated by Django 4.1 on 2022-11-02 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkup', '0004_alter_checkup_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkup',
            name='staff',
        ),
        migrations.AddField(
            model_name='checkup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
