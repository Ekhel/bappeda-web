# Generated by Django 3.2.7 on 2022-07-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0003_auto_20220704_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokumen',
            name='tahapan',
            field=models.CharField(blank=True, choices=[('rancangan awal', 'Rancangan Awal'), ('rancangan', 'Rancangan'), ('rancangan akhir', 'Rancangan Akhir')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dokumen',
            name='cover',
            field=models.ImageField(blank=True, default='dokumen/cover-default.jpeg', null=True, upload_to='dokumen_cover/'),
        ),
    ]
