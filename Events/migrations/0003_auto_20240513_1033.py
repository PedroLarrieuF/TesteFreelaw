# Generated by Django 3.2.25 on 2024-05-13 13:33

import Events.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events', '0002_auto_20240511_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 5, 13))]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(blank=True, related_name='eventos_inscritos', to=settings.AUTH_USER_MODEL, validators=[Events.models.validate_participantes_limit]),
        ),
    ]
