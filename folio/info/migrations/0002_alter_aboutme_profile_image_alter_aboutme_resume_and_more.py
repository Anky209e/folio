# Generated by Django 4.1.4 on 2023-06-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='profile_image',
            field=models.FileField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='skill_icons/'),
        ),
    ]