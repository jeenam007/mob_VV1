# Generated by Django 5.1.7 on 2025-04-01 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=70, unique=True)),
                ('price', models.IntegerField()),
                ('specs', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobileapp.brand')),
            ],
        ),
    ]
