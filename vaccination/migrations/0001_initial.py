# Generated by Django 5.0 on 2024-12-15 23:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0003_rename_end_tiem_slot_end_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('is_vaccinated', models.BooleanField(default=False)),
                ('updated_on', models.DateField(auto_now=True)),
                ('Slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.slot')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
