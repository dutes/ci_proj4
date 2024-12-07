# Generated by Django 4.0 on 2024-12-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('category', models.CharField(choices=[('Starters', 'Starters'), ('Mains', 'Mains'), ('Desserts', 'Desserts')], max_length=50)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]