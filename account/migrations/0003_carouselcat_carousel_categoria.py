# Generated by Django 4.2.6 on 2023-11-10 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_carousel_pubblicato'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome della categoria')),
            ],
        ),
        migrations.AddField(
            model_name='carousel',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.carouselcat'),
        ),
    ]