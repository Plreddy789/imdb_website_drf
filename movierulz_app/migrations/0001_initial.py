# Generated by Django 5.0.2 on 2024-02-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('hero_name', models.CharField(max_length=25)),
            ],
        ),
    ]
