# Generated by Django 3.2 on 2022-07-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
