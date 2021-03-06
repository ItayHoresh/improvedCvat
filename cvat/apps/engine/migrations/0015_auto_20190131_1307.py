# Generated by Django 2.1.3 on 2019-01-31 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0014_job_max_shape_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LabelAttrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Attrs')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LabelAttrValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelAttribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.LabelAttrs')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Vals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='labelattrvalues',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Vals'),
        ),
        migrations.AddField(
            model_name='labelattrs',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Labels'),
        ),
    ]
