# Generated by Django 2.1.3 on 2019-03-06 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0017_objectstorages_projects_projects_objectstorages_projects_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='engine.Projects'),
            preserve_default=False,
        ),
    ]
