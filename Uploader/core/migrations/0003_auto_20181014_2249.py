# Generated by Django 2.0.5 on 2018-10-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181014_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_id',
        ),
        migrations.AddField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
