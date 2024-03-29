# Generated by Django 4.2.4 on 2023-08-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_code', models.CharField(max_length=6)),
                ('account_suitability', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_code', models.CharField(max_length=6)),
                ('asset_name', models.TextField()),
                ('asset_cnpj', models.CharField(max_length=16)),
                ('class_name', models.CharField(max_length=50)),
                ('position_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_code', models.CharField(max_length=6)),
                ('account_suitability', models.CharField(max_length=30)),
                ('asset_name', models.TextField()),
                ('asset_cnpj', models.CharField(max_length=16)),
                ('class_name', models.CharField(max_length=50)),
                ('position_value', models.FloatField()),
            ],
        ),
    ]
