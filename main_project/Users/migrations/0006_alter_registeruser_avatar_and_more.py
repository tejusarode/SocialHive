# Generated by Django 5.0.7 on 2024-08-07 10:16

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_rename_caption_registeruser_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='avatar',
            field=models.CharField(choices=[('css/avatar1.png', 'Avatar 1'), ('css/avatar2.png', 'Avatar 2'), ('css/avatar3.png', 'Avatar 3'), ('css/avatar4.png', 'Avatar 4'), ('custom avatar', 'Custom Upload')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='custom_avatar',
            field=models.ImageField(blank=True, default='C:\\Users\\Tejaswini\\OneDrive\\Desktop\\FinalProject\\main_project\\Users\\media\\avatar1.png', null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/avatars/'), upload_to='avatars/'),
        ),
    ]
