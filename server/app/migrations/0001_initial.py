# Generated by Django 5.0.3 on 2024-03-28 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('nickname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('permissions', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('messageid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('content', models.CharField(max_length=255)),
                ('createdon', models.DateTimeField()),
                ('spoiler', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.member')),
            ],
        ),
    ]