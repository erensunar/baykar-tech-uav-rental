# Generated by Django 5.0.2 on 2024-02-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav_', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='is_rented',
            field=models.BooleanField(default=False, verbose_name='is Rented'),
        ),
    ]
