# Generated by Django 4.2 on 2023-05-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_medicineimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dosage_type',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
