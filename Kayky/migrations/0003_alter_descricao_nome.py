# Generated by Django 5.1 on 2024-09-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kayky', '0002_remove_pessoa_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descricao',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
