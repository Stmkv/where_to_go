# Generated by Django 4.2 on 2024-10-21 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_place_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='description_long',
        ),
    ]