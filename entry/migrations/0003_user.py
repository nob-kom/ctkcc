# Generated by Django 3.0.7 on 2020-06-22 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20200620_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower', models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C')])),
                ('room_number', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('tel_1', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号1')),
                ('tel_2', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号2')),
                ('admission_date', models.DateField()),
                ('secession_date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
