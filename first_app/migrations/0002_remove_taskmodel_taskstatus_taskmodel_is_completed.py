# Generated by Django 4.2.3 on 2023-08-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='taskStatus',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]