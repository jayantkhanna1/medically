# Generated by Django 2.2 on 2021-08-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0004_auto_20210815_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.BigIntegerField(default=8755429982),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.BigIntegerField(default=8755429982),
            preserve_default=False,
        ),
    ]
