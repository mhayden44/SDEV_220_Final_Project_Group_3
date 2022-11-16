# Generated by Django 4.1.1 on 2022-11-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0005_alter_shoe_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='photo',
        ),
        migrations.AddField(
            model_name='shoe',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
