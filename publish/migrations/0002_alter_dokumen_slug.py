# Generated by Django 3.2.7 on 2022-03-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokumen',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
