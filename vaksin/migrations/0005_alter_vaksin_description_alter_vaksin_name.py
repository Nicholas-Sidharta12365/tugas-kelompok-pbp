# Generated by Django 4.1 on 2022-10-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaksin', '0004_alter_vaksin_dose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaksin',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vaksin',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]