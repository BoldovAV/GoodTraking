# Generated by Django 4.2 on 2024-04-04 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_remove_habitnice_need_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitnice',
            name='public',
        ),
    ]