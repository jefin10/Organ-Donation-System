# Generated by Django 5.1.2 on 2024-10-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_donor_organ_parts_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
