# Generated by Django 4.1.5 on 2023-01-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
