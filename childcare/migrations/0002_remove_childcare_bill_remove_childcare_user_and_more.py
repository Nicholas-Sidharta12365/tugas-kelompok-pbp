# Generated by Django 4.1 on 2022-10-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childcare',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='childcare',
            name='user',
        ),
        migrations.AddField(
            model_name='childcare',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
