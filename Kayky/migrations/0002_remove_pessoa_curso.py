# Generated by Django 5.1 on 2024-08-31 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kayky', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='curso',
        ),
    ]
