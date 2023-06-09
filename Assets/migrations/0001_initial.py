# Generated by Django 4.1.7 on 2023-03-12 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='deviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('condition', models.CharField(max_length=255)),
                ('checked_out', models.BooleanField(default=False)),
                ('checked_out_date', models.DateTimeField(null=True)),
                ('checked_in_date', models.DateTimeField(null=True)),
                ('checked_in_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_in_devices', to='Assets.employee')),
                ('checked_out_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_out_devices', to='Assets.employee')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.company')),
            ],
        ),
    ]
