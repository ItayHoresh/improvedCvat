# Generated by Django 2.1.3 on 2019-07-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0030_auto_20190620_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='video_id',
            field=models.IntegerField(default=-1),
        ),
    ]
