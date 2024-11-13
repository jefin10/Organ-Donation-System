# Generated by Django 5.1.2 on 2024-10-31 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0011_appointments_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=250)),
                ('Appointment_date', models.DateField()),
                ('gender', models.CharField(max_length=250)),
                ('age', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=600)),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.doctor')),
            ],
        ),
    ]
