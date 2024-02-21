# Generated by Django 5.0.2 on 2024-02-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav_', '0003_uav_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='uav',
            name='description',
            field=models.TextField(default='Bos', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uav',
            name='image',
            field=models.CharField(default='', max_length=50, verbose_name='Image Path'),
        ),
    ]
