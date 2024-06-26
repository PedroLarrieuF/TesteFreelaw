# Generated by Django 3.2.25 on 2024-05-11 18:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('local', models.CharField(choices=[('Norte', 'Norte'), ('Nordeste', 'Nordeste'), ('Centro-Oeste', 'Centro-Oeste'), ('Sudeste', 'Sudeste'), ('Sul', 'Sul')], max_length=100)),
                ('hora', models.TimeField()),
                ('data', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 5, 11))])),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, help_text='Adicione o logo de seu evento.', null=True, upload_to='eventos/')),
                ('idealizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
