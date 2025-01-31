# Generated by Django 5.0.7 on 2024-08-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_follow_options_follow_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeruser',
            old_name='caption',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='registeruser',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registeruser',
            name='following_count',
            field=models.IntegerField(default=0),
        ),
    ]
