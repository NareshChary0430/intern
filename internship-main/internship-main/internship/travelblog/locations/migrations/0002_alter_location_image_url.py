# Generated by Django 4.2 on 2024-11-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]