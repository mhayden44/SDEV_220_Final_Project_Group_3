# Generated by Django 4.1.1 on 2022-11-16 17:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0007_shoe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='photo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
