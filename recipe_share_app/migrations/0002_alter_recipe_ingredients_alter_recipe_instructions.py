# Generated by Django 5.1.4 on 2024-12-15 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_share_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(max_length=5000),
        ),
    ]
