# Generated by Django 5.1.5 on 2025-01-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('DRINKS', 'Drinks'), ('DESSERT', 'Dessert'), ('SNACKS', 'Snacks'), ('MAIN_MEAL', 'Main Meal')], default='MAIN_MEAL', max_length=20),
        ),
    ]
