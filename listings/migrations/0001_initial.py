# Generated by Django 4.2.1 on 2024-10-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('body_type', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=50)),
                ('transmission_choices', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=30)),
                ('status', models.CharField(choices=[('available', 'Available'), ('rented', 'Rented'), ('maintainance', 'Under Maintainance')], default='available', max_length=20)),
                ('seats', models.PositiveIntegerField()),
                ('doors', models.PositiveIntegerField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='GHC', max_length=3)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-added_at',),
            },
        ),
    ]
