# Generated by Django 2.2 on 2021-08-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0003_auto_20210815_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='password',
            field=models.CharField(max_length=600),
        ),
    ]