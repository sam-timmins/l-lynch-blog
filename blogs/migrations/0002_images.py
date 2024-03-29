# Generated by Django 3.2 on 2022-07-24 19:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
