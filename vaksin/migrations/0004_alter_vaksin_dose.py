# Generated by Django 4.1 on 2022-10-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaksin', '0003_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaksin',
            name='dose',
            field=models.FloatField(),
        ),
    ]
