# Generated by Django 4.1 on 2022-10-29 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaksin', '0005_alter_vaksin_description_alter_vaksin_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaksin',
            old_name='description',
            new_name='side_effect',
        ),
    ]
