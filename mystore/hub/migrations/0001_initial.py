# Generated by Django 5.1 on 2024-08-29 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(blank=True, max_length=30, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CatagoryHub',
                'verbose_name_plural': 'CatagoryHubs',
            },
        ),
        migrations.CreateModel(
            name='CatagoryInitial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intial_name', models.CharField(blank=True, max_length=60, null=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.catagoryhub')),
            ],
            options={
                'verbose_name': 'CatagoryInitial',
                'verbose_name_plural': 'CatagoryInitials',
            },
        ),
        migrations.CreateModel(
            name='CatagorySecondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_name', models.CharField(blank=True, max_length=60, null=True)),
                ('catagoryInitail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.catagoryinitial')),
            ],
            options={
                'verbose_name': 'CatagorySecondary',
                'verbose_name_plural': 'CatagorySecondaries',
            },
        ),
    ]
