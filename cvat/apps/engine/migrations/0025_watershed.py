# Generated by Django 2.1.3 on 2019-05-26 08:01

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0024_auto_20190506_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watershed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.PositiveIntegerField()),
                ('paintings', django.contrib.postgres.fields.jsonb.JSONField()),
                ('watershed', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), null=True, size=None)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Task')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
