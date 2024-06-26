# Generated by Django 5.0.6 on 2024-06-14 14:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_vab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('admin', models.CharField(blank=True, choices=[('General', 'General'), ('Mayor', 'Mayor'), ('Captain', 'Captain'), ('Leytenant', 'Leytenant'), ('Serjant', 'Serjant'), ('Kursant', 'Kursant'), ('Saldat', 'Saldat')], max_length=200, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('shiori', models.CharField(blank=True, max_length=200, null=True)),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]
