# Generated by Django 5.0.4 on 2024-04-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veraz', '0002_datos'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='archivo',
            field=models.FileField(null=True, upload_to='veraz/archivos/'),
        ),
    ]