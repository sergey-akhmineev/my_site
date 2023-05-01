# Generated by Django 4.2 on 2023-05-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_medicine_availability_medicine_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='dosage',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.FloatField(),
        ),
    ]