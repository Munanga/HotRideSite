# Generated by Django 2.0.5 on 2018-10-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AddField(
            model_name='car',
            name='car_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='ride_profile_pics/'),
        ),
    ]
