# Generated by Django 2.0.6 on 2019-06-09 21:59

from django.db import migrations, models
import netdev.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Netdev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('device_type', models.CharField(max_length=30, verbose_name='Device type')),
                ('brand', models.CharField(max_length=20, verbose_name='Brand')),
                ('netdev_model', models.CharField(max_length=20, verbose_name='Model')),
                ('generation', models.CharField(blank=True, default=None, max_length=5, verbose_name='Generation')),
                ('manufacture_year', models.IntegerField(blank=True, default=None, verbose_name='Year of manufacture')),
                ('os', models.CharField(blank=True, default=None, max_length=100, verbose_name='Device image')),
                ('port_number', models.IntegerField(verbose_name='Number of physical network ports')),
                ('port_description', models.CharField(max_length=50, verbose_name='Port description')),
                ('serial_number', models.CharField(blank=True, default=None, max_length=30, verbose_name='Serial number')),
                ('warranty', models.CharField(max_length=100, verbose_name='Warranty status')),
                ('condition', models.CharField(max_length=100, verbose_name='Condition')),
                ('file_picture_1', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Front Picture')),
                ('file_picture_2', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Back Picture')),
                ('file_other', models.FileField(blank=True, default=None, upload_to=netdev.models.save_directory_path, verbose_name='Other file/Zip file if many')),
                ('other', models.TextField(max_length=2000, verbose_name='Notes')),
            ],
            options={
                'verbose_name_plural': 'Network Devices',
            },
        ),
    ]
