# Generated by Django 4.2.13 on 2024-06-01 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task_delete_userforthistool'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Цель', 'verbose_name_plural': 'Цели'},
        ),
    ]
