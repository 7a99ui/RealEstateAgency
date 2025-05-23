# Generated by Django 5.1.3 on 2024-12-02 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('property', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'appartement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('property', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'maison',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('property', models.CharField(blank=True, max_length=50, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'terrain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.IntegerField()),
                ('property_type', models.CharField(choices=[('maison', 'Maison'), ('terrain', 'Terrain'), ('appartement', 'Appartement')], max_length=20)),
                ('transaction_type', models.CharField(choices=[('achat', 'Achat'), ('vente', 'Vente')], max_length=10)),
                ('transaction_date', models.DateField()),
                ('price', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='RealEstateAgency.client')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
    ]
