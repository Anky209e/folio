# Generated by Django 4.1.4 on 2023-06-08 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('about', models.TextField(blank=True)),
                ('icon', models.FileField(upload_to='skill_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_image', models.FileField(upload_to='profile_images/')),
                ('who_am_i', models.TextField(blank=True, null=True)),
                ('what_can_i_do', models.TextField(blank=True, null=True)),
                ('resume', models.FileField(upload_to='resume/')),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.skill')),
            ],
        ),
    ]
