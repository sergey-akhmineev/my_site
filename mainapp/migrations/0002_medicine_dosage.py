# Generated by Django 4.2 on 2023-05-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dosage',
            field=models.PositiveIntegerField(default=50),
        ),
    ]