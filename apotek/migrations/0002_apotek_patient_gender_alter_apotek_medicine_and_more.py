# Generated by Django 4.1 on 2022-11-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apotek', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apotek',
            name='patient_gender',
            field=models.CharField(default='F', max_length=50),
        ),
        migrations.AlterField(
            model_name='apotek',
            name='medicine',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='apotek',
            name='patient_age',
            field=models.IntegerField(),
        ),
    ]