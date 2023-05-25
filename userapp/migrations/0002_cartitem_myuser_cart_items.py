# Generated by Django 4.2 on 2023-05-24 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_initial'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='cart_items',
            field=models.ManyToManyField(blank=True, to='userapp.cartitem'),
        ),
    ]