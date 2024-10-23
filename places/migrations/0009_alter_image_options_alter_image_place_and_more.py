# Generated by Django 4.2 on 2024-10-23 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_description_short'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number_image'], 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Достопримечательность'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
