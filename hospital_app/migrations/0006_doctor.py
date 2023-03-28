# Generated by Django 2.2 on 2021-08-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0005_auto_20210816_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=600)),
                ('can_delete', models.BooleanField(default=False)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]