# Generated by Django 4.2 on 2024-10-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description_short', models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, null=True, verbose_name='Длинное описание')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Широта')),
            ],
        ),
    ]
