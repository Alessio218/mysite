# Generated by Django 4.2.6 on 2023-11-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_carousel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='img',
            field=models.ImageField(default='slide/no_img.jpeg', upload_to='slide/%Y/%m/', verbose_name='Immagine Slide'),
        ),
    ]
