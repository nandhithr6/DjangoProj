# Generated by Django 5.1 on 2024-09-28 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_is_inspiring_recipeschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Rating must be at least 1.'), django.core.validators.MaxValueValidator(5, message='Rating cannot exceed 5.')]),
        ),
    ]
