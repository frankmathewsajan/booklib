# Generated by Django 5.0.2 on 2024-03-09 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_genres',
            field=models.ManyToManyField(to='library.genre'),
        ),
    ]