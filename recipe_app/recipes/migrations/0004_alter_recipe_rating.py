# Generated by Django 5.1 on 2024-09-28 10:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=2, validators=[django.core.validators.MinValueValidator(1.0, message='Rating must be at least 1.'), django.core.validators.MaxValueValidator(5.0, message='Rating cannot exceed 5.')]),
        ),
    ]
