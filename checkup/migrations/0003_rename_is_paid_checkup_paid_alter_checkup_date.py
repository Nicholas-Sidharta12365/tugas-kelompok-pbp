# Generated by Django 4.1 on 2022-11-02 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkup', '0002_checkup_status_checkup_type_alter_checkup_doctor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkup',
            old_name='is_paid',
            new_name='paid',
        ),
        migrations.AlterField(
            model_name='checkup',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
