# Generated by Django 5.0.2 on 2024-02-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierulz_app', '0005_alter_videoslist_platform_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.FloatField(),
        ),
    ]