# Generated by Django 5.0.6 on 2024-05-28 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armiya', '0003_alter_tasks_status_balls_historyballs_balls_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoryTasks',
        ),
    ]
