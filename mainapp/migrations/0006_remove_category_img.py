# Generated by Django 4.2 on 2023-05-25 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_medicine_dosage_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img',
        ),
    ]
